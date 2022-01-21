from rest_framework import serializers


class StadiumCreateInputSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    city_id = serializers.IntegerField(required=True)
