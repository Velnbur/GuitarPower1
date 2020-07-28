from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class TagModel(models.Model):
    tag = models.CharField(max_length=50)
    count_of_uses = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.tag


class ArticleModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=50, verbose_name="Heading", default="Heading")
    text = models.TextField(max_length=50000, verbose_name='Text', default="Text")
    date = models.DateTimeField(auto_now=True, verbose_name="Date")
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/',
                              verbose_name='Изображение',
                              default='images/test-photo.jpg',
                              null=True,
                              blank=True)
    tags = models.ManyToManyField(TagModel, blank=True)
    # все нужные поля в таблице для статьи

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
    # Как будут отображаться Статьи в админке

    def __str__(self):
        return self.heading


class CommentModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author", null=True)
    article_to = models.ForeignKey(ArticleModel, verbose_name='Article', on_delete=models.CASCADE, null=True)
    text = models.TextField(max_length=5000, verbose_name='Comment Text', default="")
    date = models.DateTimeField(auto_now=True, verbose_name="Date")
    # все нужные поля в таблице для коментариев к статьям

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return "Коментарий %s" % self.author + " к %s" % self.article_to
    # Как будут отображаться коментарии в админке


class CommentAnswerModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author", null=True)
    comment_to = models.ForeignKey(CommentModel, verbose_name='Comment to', on_delete=models.CASCADE, null=True)
    text = models.TextField(max_length=5000, verbose_name='Comment Answer Text', default="")
    date = models.DateTimeField(auto_now=True, verbose_name="Date")

    class Meta:
        verbose_name = 'Comment Answer'
        verbose_name_plural = 'Comment Answers'

    def __str__(self):
        return "Comment %s" % self.author + " to %s" % self.comment_to
