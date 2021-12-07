from .models import Stadium
from rest_framework import serializers


class StadiumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stadium
        fields = ('id', 'name', 'founded_in', 'capacity',)
