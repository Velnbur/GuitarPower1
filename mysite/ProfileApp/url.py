from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import UserLoginForm

urlpatterns = [
    path(r'', views.profile_render),
    path(r'login/',
         auth_views.LoginView.as_view(template_name="authentication/login.html",
                                      authentication_form=UserLoginForm),
         name='login'),
]