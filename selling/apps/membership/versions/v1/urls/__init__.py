from django.urls import re_path

from selling.apps.membership.versions.v1.api.api import RegisterAPIView, LoginAPIView

urlpatterns = [
    re_path(r'^login[/]?$', LoginAPIView.as_view()),
    re_path(r'^register[/]?$', RegisterAPIView.as_view())
]
