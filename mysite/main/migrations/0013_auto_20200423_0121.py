# Generated by Django 2.1.5 on 2020-04-22 23:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200409_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('imageFile', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 23, 1, 21, 15, 348511), verbose_name='date published'),
        ),
    ]