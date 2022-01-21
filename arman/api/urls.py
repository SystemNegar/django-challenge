from django.urls import include, path

app_name = "api"
urlpatterns = [
    path("", include("arman.accounts.urls", namespace="accounts")),
    path("", include("arman.stadium.urls", namespace="stadiums")),
    path("doc/", include("arman.swagger.urls")),
]
