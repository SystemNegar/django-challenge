from .serializers import SeatSerializer, ReserveSeatSerializer
from .models import Seat
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class SeatView(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = SeatSerializer
    http_method_names = ['get', 'post', 'put']
    queryset = Seat.objects.all()


class ReserveSeatView(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = ReserveSeatSerializer
    http_method_names = ['patch']

    def partial_update(self, request, *args, **kwargs):
        data = request.data
        serializer = ReserveSeatSerializer(data=data)
        if serializer.is_valid():
            reserved = serializer.save()
            return Response(ReserveSeatSerializer(reserved).data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
