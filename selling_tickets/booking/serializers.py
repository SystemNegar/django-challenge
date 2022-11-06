from rest_framework import serializers
from booking.models import Stadium, StadiumPlace, PlaceSeats, Team, Match


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
        if validated_data.get('seat_number') > number_of_row_seats_limitation:
            raise serializers.ValidationError("seledted seats is not existed for this row") 
        return super().create(validated_data)

