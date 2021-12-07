from django.urls import path, include
from django.conf.urls import url
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from stadium import urls as stadium_urls
from matches import urls as match_urls
from seats import urls as seat_urls
from authentication import urls as auth_urls


schema_view = get_schema_view(
   openapi.Info(
      title="Volleyball Federation API",
      default_version='v1',
      description="All endpoints need authentication.",
   ),
    public=True,
)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/authentication/', include(auth_urls)),
    path('api/v1/stadium/', include(stadium_urls)),
    path('api/v1/match/', include(match_urls)),
    path('api/v1/seat/', include(seat_urls)),
]
