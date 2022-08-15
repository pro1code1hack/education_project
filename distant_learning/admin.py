from django.contrib import admin
from .models import *


class AdditionalFilesInline(admin.TabularInline):
    model = AdditionalFiles
    extra = 1


@admin.register(DistantLearningLesson)
class DistantLearningLessonAdmin(admin.ModelAdmin):
    inlines = [AdditionalFilesInline]
