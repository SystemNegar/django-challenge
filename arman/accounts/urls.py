from django.urls import path

from .apis import SignupApi

app_name = "accounts"
urlpatterns = [
    path("signup/", SignupApi.as_view(), name="signup"),
]
