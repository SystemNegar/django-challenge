from django.urls import path, include
from user.views import SignUpAPI, LoginAPI
from knox import views as knox_views

urlpatterns = [
    path('', include('knox.urls')),
    path('register', SignUpAPI.as_view()),
    path('login', LoginAPI.as_view()),
    path('logout',knox_views.LogoutView.as_view(), name="knox-logout"),
]