from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from extensions.custom_permissions import CustomDjangoModelPermission

from booking.models import Section
from booking.serializers import SectionSerializer


class SectionViewSet(ModelViewSet):
    """
    ViewSet for the 'Section' model objects
    """
    serializer_class = SectionSerializer
    queryset = Section.objects.select_related('stadium').all()
    permission_classes = (CustomDjangoModelPermission,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['stadium', 'location', 'capacity', 'price']
    search_fields = ['stadium__name', 'location', 'capacity', 'price']
