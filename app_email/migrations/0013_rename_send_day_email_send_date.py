# Generated by Django 4.2.4 on 2023-09-02 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_email', '0012_alter_email_frequency_alter_email_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email',
            old_name='send_day',
            new_name='send_date',
        ),
    ]
