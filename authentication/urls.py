from django.urls import path
from authentication.views import ObtainTokenPairView, RegisterView
from rest_framework_simplejwt.views import TokenRefreshView

app_name = "authentication"

urlpatterns = [
    path('login/', ObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
]