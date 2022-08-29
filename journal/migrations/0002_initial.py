# Generated by Django 4.1 on 2022-08-29 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('journal', '0001_initial'),
        ('people', '0001_initial'),
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.lesson', verbose_name='Урок'),
        ),
        migrations.AddField(
            model_name='score',
            name='score_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.ratingitemstatus', verbose_name='Статус оценки'),
        ),
        migrations.AddField(
            model_name='score',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='score_student', to='people.student', verbose_name='Студент'),
        ),
        migrations.AddField(
            model_name='groupstudent',
            name='grade',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='group', to='journal.grade', verbose_name='Наименование класса'),
        ),
        migrations.AddField(
            model_name='groupstudent',
            name='subjects',
            field=models.ManyToManyField(to='lessons.subject'),
        ),
    ]
