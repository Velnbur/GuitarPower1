from django.shortcuts import render
from django.utils.html import strip_tags
from .models import ArticleModel, CommentModel
from .forms import SearchForm, FilterForm
from django.utils import timezone


def forum_render(request, num):
    num = num * 10

    articles = ArticleModel.objects.all()
    # иннициализация всех объектов из БД

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
    filter_form = FilterForm(request.POST)
    # иннициализация формы для фильтрации и сортировки объектов

    if request.method == "POST":
        # определение типа http запроса

        if search_form.is_valid():
            search = search_form.cleaned_data.get("search")
            articles = articles.filter(text__contains=search)
            # фильтрация объектов по наличию слова из формы

        if filter_form.is_valid():
            order = filter_form.cleaned_data.get("order_choices")
            data_from = filter_form.cleaned_data.get("pub_date_from")
            data_to = filter_form.cleaned_data.get("pub_date_to")

            if data_to:
                articles = articles.exclude(date__gte=data_to)
                # фильтрация по дате от данного числа

            if data_from:
                articles = articles.filter(date__gte=data_from)
                # фильтрация по дате до данного числа

            if order == 'from_new_to_old':
                articles = articles[::-1]
                # сортировка от новых к старым

            if order == 'most_popular':
                articles = articles.order_by('-views')
                # сортировка по количеству просмотров

    for i in articles:
        i.text = strip_tags(i.text)

    count = list(range(1, (len(articles) // 10) + 2))
    # массив с цифрами страниц

    articles = articles[num - 10:num]
    # ограничение количества объектов по 10 от num-10 до num

    context = {
        "articles": articles,
        "count": count,
        "filter_form": filter_form,
        "search_form": search_form,
        "most_popular_articles": most_popular_articles,
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
