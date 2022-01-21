from django.urls import path

from .apis import OTPApi, SignUpApi

app_name = "accounts"
urlpatterns = [
    path("signup/", SignUpApi.as_view(), name="signup"),
    path("otp/", OTPApi.as_view(), name="otp"),
]
