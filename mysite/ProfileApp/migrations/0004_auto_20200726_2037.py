# Generated by Django 3.0.8 on 2020-07-26 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProfileApp', '0003_auto_20200725_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='birth_date',
            field=models.DateField(blank=True, default='', null=True),
        ),
    ]