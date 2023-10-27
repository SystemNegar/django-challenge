from rest_framework.serializers import ModelSerializer

from booking.models import Team


class TeamSerializer(ModelSerializer):
    """
    Serializer for the 'Team' model
    """

    class Meta:
        model = Team
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
