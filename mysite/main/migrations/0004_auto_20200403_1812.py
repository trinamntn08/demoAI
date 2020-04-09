# Generated by Django 2.1.5 on 2020-04-03 16:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200403_1656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorial',
            old_name='tutorial_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='tutorial',
            old_name='tutorial_title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='tutorial_published',
        ),
        migrations.AddField(
            model_name='tutorial',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 3, 18, 12, 36, 727691), verbose_name='date published'),
        ),
    ]