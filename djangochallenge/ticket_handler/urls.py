from django.urls import path
from . import views

app_name = "main"   


urlpatterns = [
    path("reserve-seat/", views.reserve_seat, name="reserve_seat")
]