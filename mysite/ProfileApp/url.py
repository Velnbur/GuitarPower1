from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import UserLoginForm

urlpatterns = [
    path(r'', views.profile_render),
    path(r'login/', views.login_view),
    path(r'logout/', views.logout_view),
    path(r'register/', views.register_view),
    path(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
         views.activate, name='activate'),
]
