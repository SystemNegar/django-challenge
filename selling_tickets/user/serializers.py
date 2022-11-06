from rest_framework import serializers
from user.models import CustomUser
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'mobile_number', 'national_code', 'first_name', 'last_name')


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'mobile_number', 'password', 'national_code', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print(validated_data)
        user = CustomUser.objects.create_user(mobile_number=validated_data['mobile_number'], 
                                              password=validated_data['password'], 
                                              national_code=validated_data['national_code'], 
                                              first_name=validated_data['first_name'], 
                                              last_name=validated_data['last_name'])
        return user

class LoginSerializer(serializers.Serializer):
    mobile_number = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials')