from django.db import transaction
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from selling.apps.seat.models import BookSeat, Seat
from selling.apps.seat.versions.v1.serializers.seat_serializer import SeatSerializer, BookSeatSerializer
from selling.apps.seat.versions.v1.services.book_service import BookSeatService
from selling.tools.response import response_ok, response400


class BaseSeatAPIView(APIView):
    permission_classes = (IsAuthenticated,)


class SeatAPIView(BaseSeatAPIView):
    def post(self, request):
        serializer = SeatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response_ok(request, message="Seat Created successfully")

        return response400(request, error=serializer.errors)


class ReserveSeatAPIView(BaseSeatAPIView):
    def post(self, request):
        user = request.user
        seat_id = request.data["seat"]
        data = {
            "user": user.id,
            "seat": seat_id
        }
        serializer = BookSeatSerializer(data=data)
        if serializer.is_valid():
            with transaction.atomic():
                BookSeatService.create_reservation(user, seat_id)
                return response_ok(request, message="Reservation successfully done!")
        return response400(request, error=serializer.errors)
