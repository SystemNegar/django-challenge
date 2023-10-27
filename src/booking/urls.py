from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stadiums', views.StadiumViewSet, basename='stadiums')
router.register('sections', views.SectionViewSet, basename='sections')
router.register('teams', views.TeamViewSet, basename='teams')
router.register('matches', views.MatchViewSet, basename='matches')
router.register('invoices', views.InvoiceViewSet, basename='invoices')
router.register('tickets', views.TicketViewSet, basename='tickets')
router.register('payments', views.PaymentViewSet, basename='payments')

urlpatterns = router.urls
