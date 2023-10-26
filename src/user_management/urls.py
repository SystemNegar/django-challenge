from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('permissions', views.PermissionViewSet, basename='permissions')

urlpatterns = router.urls
