# Generated by Django 4.2.4 on 2023-09-01 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, verbose_name='тема письма')),
                ('message', models.TextField(verbose_name='сообщение')),
                ('frequency', models.CharField(choices=[('once', 'Единоразово'), ('daily', 'Ежедневно'), ('weekly', 'Еженедельно'), ('monthly', 'Ежемесячно')], max_length=35, verbose_name='частота')),
                ('status', models.CharField(choices=[('created', 'создана'), ('launched', 'запушена'), ('finished', 'завершена')], default=('created', 'создана'), max_length=35, verbose_name='статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='время обновления')),
                ('send_time', models.TimeField(verbose_name='время отправление')),
                ('send_day', models.DateField(verbose_name='дата отправление')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
    ]
