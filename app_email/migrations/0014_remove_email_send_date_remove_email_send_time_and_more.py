# Generated by Django 4.2.4 on 2023-09-02 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_email', '0013_rename_send_day_email_send_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='send_date',
        ),
        migrations.RemoveField(
            model_name='email',
            name='send_time',
        ),
        migrations.AddField(
            model_name='email',
            name='send_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='время и дата отправление'),
        ),
    ]
