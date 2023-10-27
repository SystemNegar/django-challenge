from django.contrib.auth.models import Permission

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ReadOnlyModelViewSet

from extensions.custom_permissions import CustomDjangoModelPermission


from user_management.serializers import PermissionSerializer


class PermissionViewSet(ReadOnlyModelViewSet):
    """
    ViewSet for the 'Permission' model objects
    """
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all().order_by('id')
    permission_classes = (CustomDjangoModelPermission,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name', 'content_type', 'codename']
    search_fields = ['name']
