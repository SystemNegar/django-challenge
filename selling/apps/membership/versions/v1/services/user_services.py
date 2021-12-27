from django.contrib.auth.models import User

from selling.apps.membership.versions.v1.serializers.user_serializer import CreateUserSerializer, UserLoginSerializer


class UserService:
    @classmethod
    def create_user(cls, params, context=True):
        user_serializer = CreateUserSerializer(data=params, context=context)
        if not user_serializer.is_valid():
            raise ValueError

        user_data = user_serializer.data
        raw_password = user_data.pop("password")

        user = User(**user_data)
        user.set_password(raw_password)
        user.save()

        data = user_serializer.data

        return data

    @classmethod
    def login_user(cls, body):
        login_serializer = UserLoginSerializer(
            data=body,
        )
        if not login_serializer.is_valid():
            raise ValueError

        return login_serializer.data
