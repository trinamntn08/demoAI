from django.contrib import admin
from .models import Tutorial,TutorialSeries,TutorialCategory
from tinymce.widgets import TinyMCE
from django.db import models

#Override Tutorial class to put some features into it
class TutorialAdmin(admin.ModelAdmin):
    fieldsets = [
            ("Title/date",{"fields":["tutorial_title","tutorial_published"]}),
            ("Content",{"fields":["tutorial_content"]})
        ]

    formfield_overrides = {
        models.TextField:{'widget':TinyMCE()}
    }

# Register your models here.
admin.site.register(TutorialCategory)
admin.site.register(TutorialSeries)
admin.site.register(Tutorial)
