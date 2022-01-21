from django.urls import include, path

app_name = "api"
urlpatterns = [
    path("accounts/", include("arman.accounts.urls", namespace="accounts")),
    path("doc/", include("arman.swagger.urls")),
]
