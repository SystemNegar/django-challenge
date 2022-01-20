from django.urls import path

from .apis import UserSignupApi

app_name = "accounts"
urlpatterns = [
    path("signup/", UserSignupApi.as_view(), name="signup"),
]
