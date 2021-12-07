from . import views
from rest_framework.routers import DefaultRouter


app_name = "seats"


router = DefaultRouter()
router.register("", views.SeatView, basename='Seat')
router.register('reserve', views.ReserveSeatView, basename='ReserveSeat')


urlpatterns = router.urls
