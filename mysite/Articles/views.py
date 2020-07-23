from django.shortcuts import render
from django.utils.html import strip_tags
from .models import ArticleModel, CommentModel, TagModel
from .forms import SearchForm
from django.utils import timezone


def forum_render(request, num, tag_name):
    num = num * 10

    articles = ArticleModel.objects.all()
    # иннициализация всех объектов из БД

    tags = TagModel.objects.all().order_by('-count_of_uses')
    # иннициализация самых популярных тегов

    most_popular_articles = articles.order_by('-views')[:5]
    # иннициализация самых просматриваемых статей
    for article in most_popular_articles:
        date = timezone.now() - article.date
        if date.days != 0:
            if date.days // 7 != 0:
                date = date.days // 7
                if date >= 4:
                    date = date // 4
                    article.date = str(date) + " months ago"
                else:
                    article.date = str(date) + " weeks ago"
            else:
                article.date = str(date.days) + " days ago"
        else:
            if date.seconds <= 60:
                article.date = "Less than a minute ago"
            elif date.seconds // 3600 > 0:
                article.date = str(date.seconds//3600) + " hours ago"
            else:
                article.date = str(date.seconds//60) + " minutes ago"
    # вывод времени для популярных статей

    search_form = SearchForm(request.POST)
    # иннициализация формы для поиска по ключевому слову

    if request.method == "POST":
        # определение типа http запроса

        if search_form.is_valid():
            search = search_form.cleaned_data.get("search")
            articles = articles.filter(text__contains=search)
            # фильтрация объектов по наличию слова из формы

    if tag_name != '_':
        articles = articles.filter(tags__tag__exact=tag_name)
    # вывод статей содержащих определёный тег

    for i in articles:
        i.text = strip_tags(i.text)
    # удаление лишнего  html код

    count = list(range(1, (len(articles) // 10) + 2))
    # массив с цифрами страниц

    articles = articles[num - 10:num]
    # ограничение количества объектов по 10 от num-10 до num

    num = num // 10

    context = {
        "articles": articles,
        "count": count,
        "search_form": search_form,
        "most_popular_articles": most_popular_articles,
        "tags": tags,
        "tag_name": tag_name,
        "num": num,
        "num_1": num+1,
        "num_2": num-1
    }

    return render(request, 'forum.html', context)


def article_render(request, num):
    articles = ArticleModel.objects.get(id__exact=num)
    comments = CommentModel.objects.filter(article_to_id=articles)
    # иннициализация статьи и комментариев

    articles.views += 1
    articles.save()
    # увеличение просмотров на 1 и сохранение его в БД

    context = {
        "article": articles,
        "num": num,
        "comments": comments,
    }
    return render(request, 'articles.html', context)
