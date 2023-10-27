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
