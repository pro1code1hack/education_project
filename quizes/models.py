from django.contrib.auth.models import User
from django.db import models
import random

DIFF_CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)

class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.ForeignKey('lessons.Topic', on_delete=models.CASCADE)
    #topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField(default=12)
    time = models.IntegerField(help_text="duration of the quiz in minutes", default=10)
    required_score_to_pass = models.IntegerField(help_text="required score in %", default=50)
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES, default='easy')
    teacher = models.CharField(max_length=50, default='Дремлюга Сергій Олександрович')

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    class Meta:
        verbose_name_plural = 'Quizes'