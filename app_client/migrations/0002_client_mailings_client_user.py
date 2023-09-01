# Generated by Django 4.2.4 on 2023-09-01 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_email', '0002_email_send_from_user_email_send_to_client'),
        ('app_client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='mailings',
            field=models.ManyToManyField(related_name='mailings', to='app_email.email', verbose_name='рассылки'),
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
    ]