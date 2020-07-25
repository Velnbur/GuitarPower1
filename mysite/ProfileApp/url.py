from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import UserLoginForm

urlpatterns = [
    path(r'', views.profile_render),
    path(r'login/', views.login_view),
    path(r'logout/', views.logout_view),
    path(r'register/', views.register_view),
]
