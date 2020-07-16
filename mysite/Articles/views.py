from django.shortcuts import render
from .models import ArticleModel, PageHit, CommentModel


def forum_render(request):
    articles = PageHit.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, 'forum.html', context)


def article_render(request, num):
    articles = ArticleModel.objects.get(id__exact=num)
    page_hit = PageHit.objects.get(article__exact=articles)
    comments = CommentModel.objects.filter(article_to_id=articles)
    page_hit.views += 1
    page_hit.save()
    context = {
        "article": articles,
        "num": num,
        "page_hit": page_hit,
        "comments": comments,
    }
    return render(request, 'articles.html', context)
