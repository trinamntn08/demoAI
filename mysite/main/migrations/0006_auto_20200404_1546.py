# Generated by Django 2.1.5 on 2020-04-04 13:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200403_1855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorial',
            old_name='content',
            new_name='tutorial_content',
        ),
        migrations.RenameField(
            model_name='tutorial',
            old_name='series',
            new_name='tutorial_series',
        ),
        migrations.RenameField(
            model_name='tutorial',
            old_name='slug',
            new_name='tutorial_slug',
        ),
        migrations.RenameField(
            model_name='tutorial',
            old_name='title',
            new_name='tutorial_title',
        ),
        migrations.RenameField(
            model_name='tutorialcategory',
            old_name='slug',
            new_name='category_slug',
        ),
        migrations.RenameField(
            model_name='tutorialcategory',
            old_name='summary',
            new_name='category_summary',
        ),
        migrations.RenameField(
            model_name='tutorialcategory',
            old_name='title',
            new_name='category_title',
        ),
        migrations.RenameField(
            model_name='tutorialseries',
            old_name='category',
            new_name='series_category',
        ),
        migrations.RenameField(
            model_name='tutorialseries',
            old_name='summary',
            new_name='series_summary',
        ),
        migrations.RenameField(
            model_name='tutorialseries',
            old_name='title',
            new_name='series_title',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='published',
        ),
        migrations.AddField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 4, 15, 46, 32, 813441), verbose_name='date published'),
        ),
    ]