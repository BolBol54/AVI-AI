# Generated by Django 3.1 on 2021-07-07 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviewers', '0008_remove_interviews_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviews',
            name='questions',
            field=models.ManyToManyField(blank=True, to='interviewers.Questions'),
        ),
    ]
