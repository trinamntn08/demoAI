from django.db import models
from datetime import datetime

# Create your models here.
class TutorialCategory(models.Model):
    category_title=models.CharField(max_length=200)
    category_summary=models.CharField(max_length=200)
    category_slug=models.CharField(max_length=200)

    class Meta:
        verbose_name_plural="Categories"

    def __str__(self):
        return self.category_title

class TutorialSeries(models.Model):
    series_title=models.CharField(max_length=200)
    series_category=models.ForeignKey(TutorialCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    series_summary=models.CharField(max_length=200)

    class Meta:
        verbose_name_plural="Series"

    def __str__(self):
        return self.series_title


# Tutorial_Class will create a tutorial model in form of Table in Database
class Tutorial(models.Model):
    tutorial_title=models.CharField(max_length=200)
    tutorial_content=models.TextField()
    tutorial_published=models.DateTimeField("date published",default=datetime.now())

    tutorial_series=models.ForeignKey(TutorialSeries,default=1,verbose_name="Series",on_delete=models.SET_DEFAULT)
    tutorial_slug=models.CharField(max_length=200,default=1)

    def __str__(self):
        return self.tutorial_title

