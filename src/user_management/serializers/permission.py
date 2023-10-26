from django.contrib.auth.models import Permission

from rest_framework.serializers import ModelSerializer


class PermissionSerializer(ModelSerializer):
    """
    Serializer for the 'Permission' model
    """

    class Meta:
        model = Permission
        fields = '__all__'
