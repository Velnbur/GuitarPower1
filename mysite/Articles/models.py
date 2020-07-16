from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class ArticleModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=50, verbose_name="Heading", default="Heading")
    text = models.TextField(max_length=50000, verbose_name='Text', default="Text")
    date = models.DateTimeField(auto_now=True, verbose_name="Date")

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.heading


class PageHit(models.Model):
    article = models.OneToOneField(ArticleModel, on_delete=models.CASCADE, default=0)
    views = models.IntegerField(default=0)


@receiver(post_save, sender=ArticleModel)
def create_article_pagehit(sender, instance, created, **kwargs):
    if created:
        PageHit.objects.create(article=instance)


class CommentModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author", null=True)
    article_to = models.ForeignKey(ArticleModel, verbose_name='Article', on_delete=models.CASCADE, null=True)
    text = models.TextField(max_length=5000, verbose_name='Comment Text', default="")
    date = models.DateTimeField(auto_now=True, verbose_name="Date")

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return "Коментарий %s" % self.author + " к %s" % self.article_to
