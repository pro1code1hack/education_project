# Generated by Django 4.1 on 2022-08-09 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='lessons',
        ),
    ]
