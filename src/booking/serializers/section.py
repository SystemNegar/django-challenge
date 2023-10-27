from rest_framework.serializers import ModelSerializer

from booking.models import Section


class SectionSerializer(ModelSerializer):
    """
    Serializer for the 'Section' model
    """

    class Meta:
        model = Section
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def to_representation(self, obj):
        data = super(SectionSerializer, self).to_representation(obj)
        data['location'] = obj.get_location_display()
        data['seat_numbers'] = obj.get_list_of_seat_numbers
        return data
