from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

# ===================================================================================================================#
from django.urls import reverse_lazy

from education_project.settings import USER_STATUS_CHOICES

AUTH_USER_MODEL = 'people.User'


class Teacher(models.Model):
    """Учитель школы."""
    username = models.CharField('Имя пользователя', max_length=130)
    group_manager = models.ForeignKey('journal.GroupStudent', verbose_name='Руководит классом',
                                      on_delete=models.SET_NULL, null=True, blank=True)
    lessons = models.ManyToManyField('lessons.Subject', related_name='teachers', verbose_name='Ведет предметы')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учитель'


class Student(models.Model):
    """Ученики школы."""
    email = models.EmailField('Почта', max_length=254, unique=True, null=True, blank=True)
    password = models.CharField('Пароль', max_length=130, default='123')
    name = models.CharField('Имя', max_length=130)
    surname = models.CharField('Фамилия', max_length=130)
    group = models.ForeignKey('journal.GroupStudent', related_name='students', verbose_name='Состоит в классе',
                              on_delete=models.CASCADE)  # не на нашу группу

    def __str__(self):
        return self.name + ' ' + self.surname + ' ' + '(група № ' + str(self.group.grade.number) + ')'

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


