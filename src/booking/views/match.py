from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from extensions.custom_permissions import CustomDjangoModelPermission

from booking.models import Match
from booking.serializers import MatchSerializer


class MatchViewSet(ModelViewSet):
    """
    ViewSet for the 'Match' model objects
    """
    serializer_class = MatchSerializer
    queryset = Match.objects.select_related('stadium', 'host_team', 'guest_team').all()
    permission_classes = (CustomDjangoModelPermission,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['stadium', 'host_team', 'guest_team', 'start_time']
    search_fields = ['stadium__name', 'host_team__name', 'guest_team__name', 'start_time']
