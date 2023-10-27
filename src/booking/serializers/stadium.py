from rest_framework.serializers import ModelSerializer

from booking.models import Stadium


class StadiumSerializer(ModelSerializer):
    """
    Serializer for the 'Stadium' model
    """

    class Meta:
        model = Stadium
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
