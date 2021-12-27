from django.urls import re_path

from selling.apps.match.versions.v1.api.api import MatchAPIView

urlpatterns = [
    re_path(r'^[/]?$', MatchAPIView.as_view()),
]
