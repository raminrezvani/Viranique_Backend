# Generated by Django 4.0.1 on 2022-10-03 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0024_alter_notificationmanager_last_seen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationmanager',
            name='title',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
