from django.shortcuts import render
from .models import ArticleModel, CommentModel


def forum_render(request):
    articles = ArticleModel.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, 'forum.html', context)


def article_render(request, num):
    articles = ArticleModel.objects.get(id__exact=num)
    comments = CommentModel.objects.filter(article_to_id=articles)
    articles.views += 1
    articles.save()
    context = {
        "article": articles,
        "num": num,
        "comments": comments,
    }
    return render(request, 'articles.html', context)
