from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import transaction
from django.db.models import Q

from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status

from booking.models import Ticket, Invoice

from extensions.choices import TicketStatusChoices, InvoiceStatusChoices


class TicketSerializer(ModelSerializer):
    """
    Serializer for the 'Ticket' model
    """

    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = ('invoice', 'status', 'created_at', 'updated_at')

    def validate(self, data):
        """
        It will use for making the validation on data
        :param data: A dict of fields
        :return: A valid data or errors
        """

        match = data.get('match')
        section = data.get('section')
        seat_number = data.get('seat_number')

        if match.start_time < timezone.now():
            raise ValidationError({
                "match": [_("The time for this match has passed!")]
            })

        if section.stadium != match.stadium:
            raise ValidationError({
                "match": [_("The stadium is not the same!")],
                "section": [_("The stadium is not the same!")]
            })

        if section.id not in match.stadium.get_section_ids:
            raise ValidationError({
                "section": [_("It does not belong to the stadium of this match!")]
            })

        if seat_number not in section.get_list_of_seat_numbers:
            raise ValidationError({
                "seat_number": [_("There is no such seat in the selected section!")]
            })

        ticket = self.Meta.model.objects.filter(
            invoice__user=self.context['request'].user,
            match=match,
            section=section,
            seat_number=seat_number
        ).first()
        if ticket:
            if ticket.status == TicketStatusChoices.SOLD:
                raise ValidationError({
                    "seat_number": [_("You have already purchased this seat number!")]
                })
            if ticket.status == TicketStatusChoices.RESERVED:
                raise ValidationError({
                    "seat_number": [_("You have already reserved this seat number, check your invoices section!")]
                })

        unavailable_seats = list(self.Meta.model.objects.filter(match=match, section=section).filter(
            Q(status=TicketStatusChoices.RESERVED) |
            Q(status=TicketStatusChoices.SOLD)
        ).values_list('seat_number', flat=True))

        if seat_number in unavailable_seats:
            raise ValidationError({
                "seat_number": [_("This seat number cannot be purchased!")]
            })

        return data

    def create(self, validated_data):
        """
        Create a new instance
        :param validated_data: A dict of fields
        :return: A new instance
        """
        with transaction.atomic():
            try:
                match = validated_data.get('match')
                section = validated_data.get('section')
                seat_number = validated_data.get('seat_number')

                invoice, created = Invoice.objects.get_or_create(
                    user=self.context['request'].user,
                    defaults={
                        'status': InvoiceStatusChoices.UNPAID
                    }
                )

                reserved_ticket = self.Meta.model.objects.create(
                    invoice=invoice,
                    match=match,
                    section=section,
                    seat_number=seat_number,
                    status=TicketStatusChoices.RESERVED
                )

                return reserved_ticket
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def to_representation(self, obj):
        data = super(TicketSerializer, self).to_representation(obj)
        data['status'] = obj.get_status_display()
        return data
