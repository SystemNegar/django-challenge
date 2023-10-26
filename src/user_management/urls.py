from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('permissions', views.PermissionViewSet, basename='permissions')
router.register('groups', views.GroupViewSet, basename='groups')

urlpatterns = router.urls
