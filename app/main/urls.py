from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_render),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('forum/', include('Articles.url')),
    path('profile/', include('Profiles.url')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
