from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from rest_framework import serializers

from user_management.serializers import GroupSerializer, PermissionSerializer


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the 'User' model
    """

    class Meta:
        model = get_user_model()
        fields = '__all__'
        read_only_fields = ('last_login', 'created_at', 'updated_at')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, value: str) -> str:
        try:
            validate_password(value, get_user_model())
            return make_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)

    def to_representation(self, obj):
        data = super(UserSerializer, self).to_representation(obj)
        data['groups'] = GroupSerializer(many=True, instance=obj.groups).data
        data['user_permissions'] = PermissionSerializer(many=True, instance=obj.user_permissions).data
        return data


class UserPasswordChangeSerializer(serializers.Serializer):
    """
    Serializer for user model password change
    """

    old_password = serializers.CharField(max_length=128, write_only=True, required=True)
    new_password1 = serializers.CharField(max_length=128, write_only=True, required=True)
    new_password2 = serializers.CharField(max_length=128, write_only=True, required=True)

    def validate_old_password(self, value):
        user = self.context['user']
        if not user.check_password(value):
            raise serializers.ValidationError(
                _('Your old password was entered incorrectly. Please enter it again.')
            )
        return value

    def validate_new_password1(self, value: str) -> str:
        try:
            validate_password(value, get_user_model())
            return value
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)

    def validate_new_password2(self, value: str) -> str:
        try:
            validate_password(value, get_user_model())
            return value
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)

    def validate(self, data):
        if data['new_password1'] != data['new_password2']:
            raise serializers.ValidationError({'new_password2': _("The two password fields didn't match.")})
        return data

    def save(self, **kwargs):
        user = self.context['user']
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user

    def to_representation(self, obj):
        data = super(UserPasswordChangeSerializer, self).to_representation(obj)
        data['groups'] = GroupSerializer(many=True, instance=obj.groups).data
        data['user_permissions'] = PermissionSerializer(many=True, instance=obj.user_permissions).data
        return data
