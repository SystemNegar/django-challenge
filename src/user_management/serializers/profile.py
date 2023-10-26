from rest_framework.serializers import ModelSerializer

from user_management.models import Profile


class ProfileSerializer(ModelSerializer):
    """
    Serializer for the 'Profile' model
    """

    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ('user', 'created_at', 'updated_at')

    def to_representation(self, obj):
        data = super(ProfileSerializer, self).to_representation(obj)
        data['gender'] = obj.get_gender_display()
        return data
