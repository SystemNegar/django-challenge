from rest_framework import serializers

from selling.apps.seat.models import Seat, BookSeat


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['name', 'match']


class BookSeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookSeat
        fields = ['seat', 'user']
