from django.contrib.auth import get_user_model

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from extensions.custom_permissions import (
    CustomDjangoModelPermission,
    UnauthenticatedPost,
    OwnProfilePermission,
    OwnUserPermission
)

from user_management.serializers import (
    UserSerializer,
    UserPasswordChangeSerializer,
    ProfileSerializer
)


class UserViewSet(ModelViewSet):
    """
    ViewSet for the 'User' model objects
    """
    serializer_class = UserSerializer
    queryset = get_user_model().objects.select_related('profile_user').all()
    permission_classes = [CustomDjangoModelPermission | UnauthenticatedPost]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['username', 'is_active', 'is_superuser', 'is_staff']
    search_fields = ['username']

    @action(
        detail=True,
        methods=["put"],
        url_path='change_password',
        url_name='change_password',
        permission_classes=[OwnUserPermission]
    )
    def change_password(self, request, pk=None):
        """
        This will use for change the current user password
        :return: The current user information
        """
        user = self.get_object()
        serializer = UserPasswordChangeSerializer(
            user,
            data=request.data,
            many=False,
            context={
                "user": user
            }
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(self.serializer_class(user).data, status=status.HTTP_200_OK)

    @action(
        detail=True,
        methods=["get"],
        url_path='user_profile',
        url_name='user_profile',
        permission_classes=[OwnProfilePermission]
    )
    def user_profile(self, request, pk=None):
        """
        This will use for getting the current user profile
        :return: The current user profile
        """
        user_profile = self.get_object().profile_user
        return Response(data=ProfileSerializer(user_profile).data, status=status.HTTP_200_OK)

    @action(
        detail=True,
        methods=["put"],
        url_path='update_user_profile',
        url_name='update_user_profile',
        permission_classes=[OwnProfilePermission]
    )
    def update_user_profile(self, request, pk=None):
        """
        This will use for change the current user profile
        :return: The current user profile
        """
        user_profile = self.get_object().profile_user
        serializer = ProfileSerializer(
            user_profile,
            data=request.data,
            many=False,
        )
        serializer.is_valid(raise_exception=True)
        user_profile = serializer.save()
        return Response(ProfileSerializer(user_profile).data, status=status.HTTP_200_OK)
