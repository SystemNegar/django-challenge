from rest_framework import serializers

from selling.apps.match.models import Match


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['name', 'stadium', 'date', 'time', 'team1', 'team2']
