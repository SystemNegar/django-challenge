from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from extensions.custom_permissions import CustomDjangoModelPermission

from booking.models import Team
from booking.serializers import TeamSerializer


class TeamViewSet(ModelViewSet):
    """
    ViewSet for the 'Team' model objects
    """
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    permission_classes = (CustomDjangoModelPermission,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']
