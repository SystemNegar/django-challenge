from rest_framework.serializers import ModelSerializer

from booking.models import Match


class MatchSerializer(ModelSerializer):
    """
    Serializer for the 'Match' model
    """

    class Meta:
        model = Match
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
