from django.shortcuts import render, redirect
from django.utils.html import strip_tags
from .models import ArticleModel, CommentModel, TagModel
from .forms import SearchForm, ArticleForm, CommentForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def date_out(articles):
    '''Выводит в формате строки время прошедшее с момента создания статьи'''
    for article in articles:
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
    return articles


'''
Вьюшки страниц
'''


def forum_render(request, num, tag_name):
    num = num * 10

    articles = ArticleModel.objects.all()
    # иннициализация всех объектов из БД

    tags = TagModel.objects.all().order_by('-count_of_uses')
    # иннициализация самых популярных тегов

    most_popular_articles = articles.order_by('-views')[:5]
    # иннициализация самых просматриваемых статей

    most_popular_articles = date_out(most_popular_articles)
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
        "num_2": num-1,
        "len_count": len(count),
    }

    return render(request, 'forum.html', context)


def add_article(request):
    user = request.user
    my_articles = ArticleModel.objects.all().filter(author__exact=user)

    # удаление лишнего  html код
    for i in my_articles:
        i.text = strip_tags(i.text)
        i.text = i.text[0:200]

    if request.method == 'POST':
        article_form = ArticleForm(request.POST)

        if article_form.is_valid():
            post = article_form.save(commit=False)
            post.author = user
            post.save()
            return redirect('/forum/add_article')

    else:
        article_form = ArticleForm()

    context = {
        "article_form": article_form,
        "user": user,
        "my_articles": my_articles,
    }

    return render(request, 'add_article.html', context)


def article_render(request, num):
    article = ArticleModel.objects.get(id__exact=num)
    comments = CommentModel.objects.filter(article_to_id=article)
    # иннициализация статьи и комментариев

    article.views += 1
    article.save()
    # увеличение просмотров на 1 и сохранение числа в БД

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            post = comment_form.save(commit=False)
            post.author = request.user
            post.article_to = article
            post.save()

    else:
        comment_form = CommentForm()

    context = {
        "article": article,
        "num": num,
        "comments": comments,
        "comment_form": comment_form,
    }
    return render(request, 'articles.html', context)


@login_required
def change_article(request, num):
    article = ArticleModel.objects.get(id__exact=num)
    if article.author == request.user:
        if request.method == 'POST':
            article_form = ArticleForm(request.POST)

            if article_form.is_valid():
                post = article_form.save(commit=False)
                post.author = request.user
                post.views = article.views
                post.date = article.date
                post.save()
                return redirect('/profile/')

        else:
            article_form = ArticleForm()
            article_form.fields['heading'].widget.attrs['value'] = article.heading
            article_form.fields['text'].widget.attrs['value'] = article.text

        context = {
            "article": article,
            "article_form": article_form,
        }

        return render(request, 'change_article.html', context)
    else:
        return redirect('/profile/')
