# Generated by Django 3.0.8 on 2020-07-29 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProfileApp', '0006_profilemodel_date_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='is_online',
            field=models.BooleanField(default=False),
        ),
    ]
