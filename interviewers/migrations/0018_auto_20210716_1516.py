# Generated by Django 3.1 on 2021-07-16 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviewers', '0017_applicants_invitationlink'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicants',
            name='state',
        ),
        migrations.AddField(
            model_name='interviewees',
            name='state',
            field=models.CharField(default='waiting', max_length=100),
        ),
    ]
