# Generated by Django 3.0.8 on 2020-07-28 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Articles', '0011_auto_20200721_2047'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentAnswerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='', max_length=5000, verbose_name='Comment Answer Text')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Date')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('comment_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Articles.CommentModel', verbose_name='Comment to')),
            ],
            options={
                'verbose_name': 'Comment Answer',
                'verbose_name_plural': 'Comment Answers',
            },
        ),
    ]
