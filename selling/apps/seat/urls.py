from django.urls import re_path, include
from selling.apps.seat.versions.v1 import urls as api_urls

urlpatterns = [
    re_path(r'^api/', include(api_urls))
]
