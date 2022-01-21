from rest_framework.routers import DefaultRouter

from .apis import StadiumApi

app_name = "stadiums"
router = DefaultRouter()
router.register(
    r"",
    StadiumApi,
    basename="stadiums",
)

urlpatterns = router.urls
