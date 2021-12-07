from .models import Seat
from rest_framework import serializers


class SeatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seat
        fields = ('match', 'row', 'column', 'seat_num', )


class ReserveSeatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seat
        fields = ('reserved', 'match', 'seat_num', 'column', 'row')

    def validate(self, data):
        reserve_seat = Seat.objects.filter(match=data.get("match"), seat_num=data.get("seat_num"), reserved__isnull=False)
        if reserve_seat.exists():
            raise serializers.ValidationError("This seat has been reserved!")
        return data
