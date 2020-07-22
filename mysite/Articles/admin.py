from django.contrib import admin
from . import models
from django_summernote.admin import SummernoteModelAdmin


class ArticleModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)


admin.site.register(models.ArticleModel, ArticleModelAdmin)
admin.site.register(models.CommentModel)
admin.site.register(models.TagModel)
