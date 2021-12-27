from rest_framework import serializers

from selling.apps.stadium.models import Stadium


class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = ['name', 'capacity']