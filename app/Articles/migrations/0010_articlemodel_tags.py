# Generated by Django 3.0.8 on 2020-07-21 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0009_remove_articlemodel_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlemodel',
            name='tags',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Articles.TagModel'),
        ),
    ]
