# Generated by Django 2.1.5 on 2020-04-03 09:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_publised',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 3, 11, 11, 51, 756997), verbose_name='date published'),
        ),
    ]