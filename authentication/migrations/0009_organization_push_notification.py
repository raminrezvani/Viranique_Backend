# Generated by Django 4.0.1 on 2022-08-23 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_remove_user_automation_remove_user_language_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='push_notification',
            field=models.BooleanField(default=False),
        ),
    ]
