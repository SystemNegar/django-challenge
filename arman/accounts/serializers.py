from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers


class SignupInputSerializer(serializers.Serializer):
    phone = PhoneNumberField(required=True)


class OTPInputSerializer(serializers.Serializer):
    phone = PhoneNumberField(required=True)
