# Generated by Django 4.0.1 on 2022-09-10 15:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0023_alter_notificationmanager_last_seen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationmanager',
            name='last_seen',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
