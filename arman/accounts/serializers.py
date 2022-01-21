from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers


class UserSignupInputSerializer(serializers.Serializer):
    phone = PhoneNumberField(required=True)
