# Generated by Django 3.1 on 2021-07-17 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviewers', '0019_auto_20210717_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='description',
            field=models.CharField(default='', max_length=300),
        ),
    ]
