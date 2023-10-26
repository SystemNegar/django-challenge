from django.contrib.auth.models import Group, Permission

from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from user_management.serializers import PermissionSerializer


class GroupSerializer(ModelSerializer):
    """
    Serializer for the 'Group' model
    """

    permissions = PermissionSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions',)


class CreateGroupSerializer(ModelSerializer):
    """
    Serializer for creating a new 'Group' instance
    """

    permissions = PermissionSerializer(many=True, read_only=True)
    permission_ids = PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=Permission.objects.all()
    )

    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions', 'permission_ids',)

    def create(self, validated_data):
        """
        Create a new instance
        :param validated_data: A dict of fields
        :return: A new instance
        """

        permission_ids = validated_data.pop('permission_ids')
        group = Group.objects.create(**validated_data)
        group.permissions.set(permission_ids)

        return group

    def update(self, instance, validated_data):
        """
        Update exists instance
        :param instance: Current instance
        :param validated_data: A dict of fields
        :return: Current instance with changes
        """

        # Get the permission ids
        permission_ids = validated_data.pop('permission_ids', [item.id for item in instance.permissions.all()])

        # Update the 'name' field
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        # Update the permissions
        instance.permissions.clear()
        instance.permissions.add(*permission_ids)

        return instance
