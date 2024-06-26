# Generated by Django 4.0.1 on 2022-07-30 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0015_alter_notificationmanager_action_object_content_type'),
        ('automation', '0002_remove_automatictile_counter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automatictile',
            name='alarm',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notifications.notificationmanager'),
        ),
        migrations.AlterField(
            model_name='manualtile',
            name='alarm',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notifications.notificationmanager'),
        ),
        migrations.DeleteModel(
            name='AutomationNotification',
        ),
    ]
