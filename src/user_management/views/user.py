from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from extensions.custom_permissions import CustomDjangoModelPermission, UnauthenticatedPost
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
    queryset = get_user_model().objects.all().order_by('id')
    permission_classes = [CustomDjangoModelPermission | UnauthenticatedPost]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['username', 'is_active', 'is_superuser', 'is_staff']
    search_fields = ['username']

    @action(detail=True, methods=["put"], url_path='change_password', url_name='change_password')
    def change_password(self, request, pk=None):
        """
        This will use for change the current user password
        :return: The current user information
        """
        try:
            pk = int(pk)
        except ValueError:
            return Response(
                {"error": _("It's not a valid pk!")},
                status=status.HTTP_404_NOT_FOUND
            )

        if self.request.user.pk != pk:
            return Response(
                {"error": _("You can't change another user's password with this method!")},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            serializer = UserPasswordChangeSerializer(
                self.request.user,
                data=request.data,
                many=False,
                context={
                    "user": self.request.user
                }
            )
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            return Response(self.serializer_class(user).data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], url_path='user_profile', url_name='user_profile')
    def user_profile(self, request):
        """
        This will use for getting the current user profile
        :return: The current user profile
        """
        return Response(data=ProfileSerializer(request.user.user_profile_user).data, status=status.HTTP_200_OK)
