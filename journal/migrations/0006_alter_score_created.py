# Generated by Django 4.1 on 2022-08-09 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0005_remove_grade_symbol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='created',
            field=models.DateField(auto_now_add=True, verbose_name='Дата создания'),
        ),
    ]
