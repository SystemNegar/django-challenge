from django.utils.translation import gettext_lazy as _
from django.db import transaction

from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status

from booking.models import Payment

from extensions.choices import InvoiceStatusChoices, PaymentStatusChoices

from decimal import Decimal


class PaymentSerializer(ModelSerializer):
    """
    Serializer for the 'Payment' model
    """

    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ('status', 'created_at')

    def validate(self, data):
        """
        It will use for making the validation on data
        :param data: A dict of fields
        :return: A valid data or errors
        """

        invoice = data.get('invoice')
        amount = data.get('amount')

        if invoice.user != self.context['request'].user:
            raise ValidationError({
                "invoice": [_("This invoice does not belong to you!")]
            })

        if invoice.status == InvoiceStatusChoices.PAID:
            raise ValidationError({
                "invoice": [_("This invoice has already been paid!")]
            })

        if invoice.get_total_amount != Decimal(amount):
            raise ValidationError({
                "amount": [_("The entered amount is not equal to the invoice amount!")]
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
                invoice = validated_data.get('invoice')

                payment_instance = self.Meta.model.objects.create(
                    invoice=invoice,
                    amount=invoice.get_total_amount,
                    status=PaymentStatusChoices.SUCCESSFUL
                )

                invoice.set_as_paid()

                return payment_instance
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def to_representation(self, obj):
        data = super(PaymentSerializer, self).to_representation(obj)
        data['status'] = obj.get_status_display()
        return data
