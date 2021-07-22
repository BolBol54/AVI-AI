# Generated by Django 3.1 on 2021-07-07 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interviewers', '0012_delete_intervquest'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterviewQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interviewers.interviews')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interviewers.questions')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
