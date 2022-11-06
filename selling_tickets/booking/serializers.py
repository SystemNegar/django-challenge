from rest_framework import serializers
from booking.models import Stadium, StadiumPlace, PlaceSeats


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
        if validated_data.get('row_number') > place_number_of_rows_limitation:
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

