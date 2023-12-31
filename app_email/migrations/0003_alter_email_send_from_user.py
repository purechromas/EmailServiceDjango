# Generated by Django 4.2.4 on 2023-09-01 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_email', '0002_email_send_from_user_email_send_to_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='send_from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='отправитель'),
        ),
    ]
