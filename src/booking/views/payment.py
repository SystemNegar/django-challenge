from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin

from extensions.custom_permissions import CustomDjangoModelPermission

from booking.models import Payment
from booking.serializers import PaymentSerializer


class PaymentViewSet(ListModelMixin, RetrieveModelMixin, CreateModelMixin, GenericViewSet):
    """
    ViewSet for the 'Payment' model objects
    """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.select_related('invoice').all()
    permission_classes = (CustomDjangoModelPermission,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['invoice', 'amount', 'status', 'created_at']
    search_fields = ['invoice', 'invoice__user__username', 'amount', 'created_at']
