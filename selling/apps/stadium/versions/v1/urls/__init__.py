from django.urls import re_path

from selling.apps.stadium.versions.v1.api.api import StadiumAPIView

urlpatterns = [
    re_path(r'^[/]?$', StadiumAPIView.as_view()),
]
