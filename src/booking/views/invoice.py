from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ReadOnlyModelViewSet

from extensions.custom_permissions import CustomDjangoModelPermission

from booking.models import Invoice
from booking.serializers import InvoiceSerializer


class InvoiceViewSet(ReadOnlyModelViewSet):
    """
    ViewSet for the 'Invoice' model objects
    """
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.select_related('user').all()
    permission_classes = (CustomDjangoModelPermission,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['user', 'status']
    search_fields = ['user__username']
