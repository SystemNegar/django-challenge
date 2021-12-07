from . import views
from rest_framework.routers import DefaultRouter


app_name = "stadium"


router = DefaultRouter()
router.register("", views.StadiumView, basename='Stadium')


urlpatterns = router.urls