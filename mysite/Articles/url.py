from django.urls import path
from . import views

urlpatterns = [
    path('<int:num>', views.forum_render),
    path('articles<int:num>', views.article_render),
]