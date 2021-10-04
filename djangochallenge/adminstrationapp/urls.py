from django.urls import path
from . import views

app_name = "main"   


urlpatterns = [
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("add-stadium/", views.add_stadium, name='add-stadium'),
    path("add-match/", views.add_match, name='add-match'),
    path("add-seat/", views.add_seat, name='add-seat')
]