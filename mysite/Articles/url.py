from django.urls import path
from . import views

urlpatterns = [
    path(r'<int:num>tag=<slug:tag_name>', views.forum_render),
    path('articles<int:num>', views.article_render),
]