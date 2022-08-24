from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.
from django.utils import timezone

from lessons.utils import get_lesson_file


class DistantLearningLesson(models.Model):
    topic = models.CharField(max_length=200)
    subject = models.ForeignKey('lessons.Subject', on_delete=models.CASCADE, null=True, blank=True)
    #group = models.ForeignKey('journal.GroupStudent', on_delete=models.CASCADE)
    course = models.IntegerField(choices=[(1, '1'), (2, '2')], default=1)
    main_text = models.TextField(max_length=3000)
    link = models.URLField(blank=True, null=True)
    additional_text = models.TextField(max_length=3000, blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey('people.Teacher', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.topic


class AdditionalFiles(models.Model):
    distant_learning_lesson = models.ForeignKey(DistantLearningLesson, default=None, on_delete=models.CASCADE)
    file = models.FileField(upload_to='lesson_files_upload', null=True, validators=[FileExtensionValidator
                            (allowed_extensions=['doc', 'pptx', 'xls', 'csv'])])
    date_uploaded = models.DateTimeField(default=timezone.now)
