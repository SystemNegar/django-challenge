from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stadiums', views.StadiumViewSet, basename='stadiums')

urlpatterns = router.urls
