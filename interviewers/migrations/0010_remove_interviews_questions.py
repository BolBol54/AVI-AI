# Generated by Django 3.1 on 2021-07-07 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interviewers', '0009_interviews_questions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interviews',
            name='questions',
        ),
    ]
