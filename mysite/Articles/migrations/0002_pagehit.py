# Generated by Django 3.0.8 on 2020-07-15 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageHit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('views', models.IntegerField(default=0)),
                ('article', models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='Articles.ArticleModel')),
            ],
        ),
    ]
