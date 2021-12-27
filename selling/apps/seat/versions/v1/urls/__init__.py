from django.urls import re_path

from selling.apps.seat.versions.v1.api.api import SeatAPIView, ReserveSeatAPIView

urlpatterns = [
    re_path(r'^[/]?$', SeatAPIView.as_view()),
    re_path(r'^reserve[/]?$', ReserveSeatAPIView.as_view()),
]
