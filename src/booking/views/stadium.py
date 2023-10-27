from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from extensions.custom_permissions import CustomDjangoModelPermission

from booking.models import Stadium
from booking.serializers import StadiumSerializer


class StadiumViewSet(ModelViewSet):
    """
    ViewSet for the 'Stadium' model objects
    """
    serializer_class = StadiumSerializer
    queryset = Stadium.objects.prefetch_related('section_stadiums').all()
    permission_classes = (CustomDjangoModelPermission,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name', 'province', 'city']
    search_fields = ['name', 'province', 'city', 'address']
