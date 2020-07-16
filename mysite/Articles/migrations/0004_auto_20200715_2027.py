# Generated by Django 3.0.8 on 2020-07-15 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0003_commentmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlemodel',
            options={'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
        migrations.AlterModelOptions(
            name='commentmodel',
            options={'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='article_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Articles.ArticleModel', verbose_name='Article'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='text',
            field=models.TextField(default='', max_length=5000, verbose_name='Comment Text'),
        ),
    ]
