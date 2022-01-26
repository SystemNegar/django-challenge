from rest_framework.routers import DefaultRouter

from .apis import CityApi

app_name = "stadiums"
router = DefaultRouter()
router.register(
    r"",
    CityApi,
    basename="cities",
)

urlpatterns = router.urls
