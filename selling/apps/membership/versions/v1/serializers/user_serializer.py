from rest_framework import serializers


class CreateUserSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=255,
        required=False,
    )
    username = serializers.CharField(
        max_length=255,
        required=True,
    )
    email = serializers.EmailField(
        max_length=255,
        required=False,
    )

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(max_length=255, required=True)
    remember_me = serializers.BooleanField(required=False)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
