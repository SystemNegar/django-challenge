from django.db.models import ProtectedError
from django.contrib.auth.models import Group

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from extensions.custom_permissions import CustomDjangoModelPermission

from user_management.serializers import GroupSerializer, CreateGroupSerializer


class GroupViewSet(ModelViewSet):
    """
    ViewSet for the 'Group' model objects
    """
    serializer_class = GroupSerializer
    queryset = Group.objects.all().order_by('id')
    permission_classes = (CustomDjangoModelPermission,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('name',)
    search_fields = ['name']

    def get_serializer_class(self):
        return CreateGroupSerializer if self.action in ('create', 'partial_update') else GroupSerializer

    def destroy(self, request, *args, **kwargs):
        users_in_this_group = self.get_object().user_set.all()
        if users_in_this_group.count() > 0:
            raise ProtectedError(
                msg="Cannot delete this instance of model 'Group' due to protected foreign keys.",
                protected_objects=users_in_this_group
            )
        else:
            return super().destroy(request, *args, **kwargs)
