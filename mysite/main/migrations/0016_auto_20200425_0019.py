# Generated by Django 2.1.5 on 2020-04-24 22:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20200424_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 25, 0, 19, 1, 682798), verbose_name='date published'),
        ),
    ]