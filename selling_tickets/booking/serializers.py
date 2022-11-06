from django.db.models import Q
from rest_framework import serializers
from booking.models import Stadium, StadiumPlace, PlaceSeats, Team, Match, Ticket, Invoice


class MatchSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    tickets = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='ticket_detail')
    class Meta:
        model = Match
        fields = '__all__'


class PlaceSeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceSeats
        fields = ('id', 'number_of_seats_per_row', 'row_number', 'place',)

    def create(self, validated_data):
        place = validated_data.get('place')
        place_number_of_rows_limitation = place.number_of_rows
        if validated_data.get('row_number') > place_number_of_rows_limitation: # validate that selected row is existed in range of rows limiation 
            raise serializers.ValidationError("seledted row is not existed for this place")
        return super().create(validated_data)


class StadiumPlaceSerializer(serializers.ModelSerializer):
    place_seats = PlaceSeatsSerializer(many=True, read_only=True)

    class Meta:
        model = StadiumPlace
        fields = ('id', 'name', 'number_of_rows', 'stadium', 'place_seats',)


class StadiumSerializer(serializers.ModelSerializer):
    places = StadiumPlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Stadium
        fields = ('id', 'name', 'city', 'address', 'places', 'matches',)


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name',)


class TicketSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)
    last_update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = Ticket
        fields = ('id', 'stadium', 'match', 'status', 'last_update_time', 'row_number', 'seat_number', 'place', 'price')
    
    def create(self, validated_data):
        selected_row_number = validated_data.get('row_number')
        place_seats = PlaceSeats.objects.get(row_number=selected_row_number)
        number_of_row_seats_limitation = place_seats.number_of_seats_per_row
        if validated_data.get('seat_number') > number_of_row_seats_limitation: # validate that the seat number is existed in range of number of seats limitation
            raise serializers.ValidationError("seledted seats is not existed for this row") 
        return super().create(validated_data)


class InvoiceSerilizer(serializers.ModelSerializer):
    tickets = serializers.PrimaryKeyRelatedField(many=True, queryset=Ticket.objects.filter(~Q(status=Ticket.RESERVED)))
    
    class Meta:
        model = Invoice
        fields = ('id', 'tickets')

    def create(self, validated_data):
        tickets = validated_data.get('tickets')
        for t in tickets:
            if t.status == Ticket.RESERVED:
                raise serializers.ValidationError("selected ticket %s is reserved" % (t.id))
        return super().create(validated_data)


    def update(self, instance, validated_data):
        tickets = validated_data.get('tickets')
        for t in tickets:
            if t.status == Ticket.RESERVED:
                raise serializers.ValidationError("selected ticket %s is reserved" % (t.id))
        return super().update(instance, validated_data)


class RetrieveInvoiceSerilizer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True)
    tickets_total_price = serializers.SerializerMethodField()

    class Meta:
        model = Invoice
        fields = ('id', 'tickets', 'tickets_total_price')

    def get_tickets_total_price(self, obj):
        return sum([t.price for t in obj.tickets.all()])


class BuyInvoiceSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ('id',)

    def update(self, instance, validated_data):
        # meaning do the payment but before that 
        # get invoice instance , get invoice tickets, check status of tickets 
        # if they are not reserved we will change their status to reservered ,
        # change status of invoice to in progress, generate payment_id and payment_date
        # and then call payment method
        # payment gateway should call my callback method for alerting the result #TODO: callback method is not implemented
        # TODO: we should handle reserverd tickets after 15 min (default duration for payment) in another job (such as celery job)
        tickets = instance.tickets.all()
        for t in tickets:
            t.reserve_ticket()
        instance.set_in_progress()
        instance.set_payment_number()

        return super().update(instance, validated_data)