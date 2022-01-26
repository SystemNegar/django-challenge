from django.urls import include, path

app_name = "api"
urlpatterns = [
    path("accounts/", include("arman.accounts.urls", namespace="accounts")),
    path("stadiums/", include("arman.stadium.urls", namespace="stadiums")),
    path("cities/", include("arman.city.urls", namespace="cities")),
    path("doc/", include("arman.swagger.urls")),
]
