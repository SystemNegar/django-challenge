from .models import Match
from rest_framework import serializers


class MatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Match
        fields = ('stadium', 'event_date', 'team1', 'team2',)

    def validate_event_date(self, event_date):
        check_event = Match.is_reserved(event_date)
        if not check_event:
            raise serializers.ValidationError({'event_date': 'Can not set this match! Change the datetime'})
        return event_date
