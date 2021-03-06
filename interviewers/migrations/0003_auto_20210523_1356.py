# Generated by Django 3.1 on 2021-05-23 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interviewers', '0002_auto_20210513_2333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='descroption',
            new_name='description',
        ),
        migrations.AddField(
            model_name='job',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.datetime_safe.datetime.now),
        ),
        migrations.AddField(
            model_name='job',
            name='created_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='createdBy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='job',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=django.utils.datetime_safe.datetime.now),
        ),
        migrations.AlterField(
            model_name='interviews',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.datetime_safe.datetime.now),
        ),
        migrations.AlterField(
            model_name='interviews',
            name='created_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='interviews',
            name='questions',
            field=models.ManyToManyField(blank=True, to='interviewers.Questions'),
        ),
        migrations.AlterField(
            model_name='interviews',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=django.utils.datetime_safe.datetime.now),
        ),
        migrations.CreateModel(
            name='CompanyUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companyUsers', to='interviewers.companies')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companyUsers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
