# Generated by Django 4.2.4 on 2023-09-02 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_email', '0010_alter_email_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='status',
            field=models.CharField(choices=[('CREATED', 'СОЗДАНА'), ('LAUNCHED', 'ЗАПУШЕНА'), ('FINISHED', ' ЗАВЕРШЕНА')], default='CREATED', max_length=30, verbose_name='статус'),
        ),
    ]
