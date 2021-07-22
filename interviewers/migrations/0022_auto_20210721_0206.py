# Generated by Django 3.1 on 2021-07-21 00:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviewers', '0021_auto_20210718_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantques',
            name='videoAns',
            field=models.FileField(null=True, upload_to='videos/', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='interviews',
            name='Expiration_date',
            field=models.DateTimeField(default=datetime.date(2021, 7, 24)),
        ),
    ]