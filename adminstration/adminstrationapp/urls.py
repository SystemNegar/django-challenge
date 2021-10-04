from django.urls import path
from . import views

app_name = "main"   


urlpatterns = [
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login")
]