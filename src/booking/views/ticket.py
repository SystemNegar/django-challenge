from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin

from extensions.custom_permissions import CustomDjangoModelPermission

from booking.models import Ticket
from booking.serializers import TicketSerializer


class TicketViewSet(ListModelMixin, RetrieveModelMixin, CreateModelMixin, GenericViewSet):
    """
    ViewSet for the 'Ticket' model objects
    """
    serializer_class = TicketSerializer
    queryset = Ticket.objects.select_related('invoice', 'match', 'section').all()
    permission_classes = (CustomDjangoModelPermission,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['invoice', 'match', 'section', 'seat_number', 'status']
    search_fields = ['invoice', 'invoice__user__username', 'match', 'section', 'seat_number']
