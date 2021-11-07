from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path(r'', views.profile_render, name='profile'),
    path(r'login/', views.login_view, name='login'),
    path(r'logout/', views.logout_view, name='logout'),
    path(r'register/', views.register_view, name='register'),
    path(r'change_profile', views.change_profile, name='change_profile'),

    path(r'activate/<uidb64>/<token>/',
         views.activate, name='activate'),

    path(r'password_reset/',
         auth_views.PasswordResetView.as_view(template_name='authentication/password_reset.html'),
         name='password_reset'),

    path(r'password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='authentication/password_reset_done.html'),
         name='password_reset_done'),

    path(r'reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='authentication/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path(r'reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='authentication/password_reset_complete.html'),
         name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
