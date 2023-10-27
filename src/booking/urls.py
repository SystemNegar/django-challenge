from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stadiums', views.StadiumViewSet, basename='stadiums')
router.register('sections', views.SectionViewSet, basename='sections')

urlpatterns = router.urls
