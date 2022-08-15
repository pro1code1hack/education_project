from django.db import models

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# from django_journal.settings import SCORE_CHOICES, STUDENT, TEACHER

# from people.models import Student, Teacher

from education_project.settings import SCORE_CHOICES

# class Lesson(models.Model):
#     """Справочник всех уроков в школе."""
#     name = models.CharField('Название', max_length=100)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'предмет'
#         verbose_name_plural = 'Справочник предметов'
from lessons.models import Lesson
from people.models import Student


class Grade(models.Model):
    """Справочник всех существующих абравиатур классов."""
    number = models.SmallIntegerField('Цифра')

    # symbol = models.CharField('Символ', max_length=1)
    # lessons = models.ManyToManyField(Lesson, related_name='grade', verbose_name='Уроки класса')

    def __str__(self):
        return f'{self.number}'

    class Meta:
        verbose_name = 'класс'
        verbose_name_plural = 'Справочник классов'


class RatingItemStatus(models.Model):
    """Справочник статусов оценок: обычная, годовая, четверть, отменено."""
    name = models.CharField('Статус оценки', max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'статус оценки'
        verbose_name_plural = 'Справочник статусов оценок'


class GroupStudent(models.Model):
    """Группы студентов."""
    grade = models.OneToOneField(Grade, related_name='group', on_delete=models.CASCADE,
                                 verbose_name='Наименование класса')
    create_group = models.DateField('Дата создания группы учеников', auto_now_add=True, blank=True, null=True)
    updated = models.DateField('Дата обновления', auto_now=True, null=True, blank=True)
    created = models.DateField('Дата создания', auto_now_add=True, null=True, blank=True)
    # specialty = models.ForeignKey('educational_institution.Specialty', on_delete=models.CASCADE, blank=True, null=True)
    subjects = models.ManyToManyField('lessons.Subject')
    # teacher = models.ForeignKey('people.Teacher', on_delete=models.CASCADE, blank=True, null=True)
    course = models.IntegerField(choices=[(i, i) for i in range(1, 3)], default=1, blank=True, null=True)

    def __str__(self):
        return self.grade.__str__()

    def get_absolute_url(self):
        return reverse_lazy('group_student_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Група учеников'
        verbose_name_plural = 'Группы учеников'


class Score(models.Model):
    """Журнал оценок."""
    group = models.ForeignKey(GroupStudent, on_delete=models.CASCADE, verbose_name='Наименование класса')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Предмет')
    student = models.ForeignKey(Student, related_name='score_student', on_delete=models.CASCADE, verbose_name='Студент',
                                blank=True, null=True)
    score = models.SmallIntegerField(choices=SCORE_CHOICES, verbose_name='Оценка')
    score_status = models.ForeignKey(RatingItemStatus, on_delete=models.CASCADE, verbose_name='Статус оценки')
    created = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return 'Оцінка:' + str(self.score) + '\t Урок: \t' + str(self.lesson) + '\t Студент: ' + str(self.student) + '---' + str(self.created)

    # TODO продумать куда вести юзера на endpoint
    def get_absolute_url(self):
        return reverse_lazy('score_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'запись журнала'
        verbose_name_plural = 'Оценки'
        # unique_together = ['student', 'lesson', 'created']
