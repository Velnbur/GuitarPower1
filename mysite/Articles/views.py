from django.shortcuts import render
from .models import ArticleModel, CommentModel
from .forms import SearchForm, FilterForm


def forum_render(request, num):
    num = num * 10

    articles = ArticleModel.objects.all()
    # иннициализация всех объектов из БД
    search_form = SearchForm(request.POST)
    # иннициализация формы для поиска по ключевому слову
    filter_form = FilterForm(request.POST)
    # иннициализация формы для фильтрации и сортировки объектов

    if request.method == "POST":
        # определение типа http запроса

        if search_form.is_valid():
            search = search_form.cleaned_data.get("search")
            articles = articles.filter(article__text__contains=search)
            # фильтрация объектов по наличию слова из формы

        if filter_form.is_valid():
            order = filter_form.cleaned_data.get("order_choices")
            data_from = filter_form.cleaned_data.get("pub_date_from")
            data_to = filter_form.cleaned_data.get("pub_date_to")

            if data_to:
                articles = articles.exclude(article__date__gte=data_to)
                # фильтрация по дате от данного числа

            if data_from:
                articles = articles.filter(article__date__gte=data_from)
                # фильтрация по дате до данного числа

            if order == 'from_new_to_old':
                articles = articles[::-1]
                # сортировка от новых к старым

            if order == 'most_popular':
                articles = articles.order_by('-views')
                # сортировка по количеству просмотров

    articles = articles[num - 10:num]
    # ограничение количества объектов по 10 от num-10 до num
    count = [i + 1 for i in range(len(articles) // 10 + 1)]
    # массив с цифрами

    context = {
        "articles": articles,
        "count": count,
        "filter_form": filter_form,
        "search_form": search_form,
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
