from django.urls import path
from . import views

urlpatterns = [
    path(r'<int:num>tag=<slug:tag_name>/', views.forum_render),
    path(r'articles<int:num>/', views.article_render),
    path(r'add_article/', views.add_article),
    path(r'change_article<int:num>/', views.change_article),
]