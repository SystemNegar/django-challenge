from . import views
from rest_framework.routers import DefaultRouter


app_name = "matches"


router = DefaultRouter()
router.register("", views.MatchView, basename='Match')


urlpatterns = router.urls