# Generated by Django 4.0.1 on 2022-07-31 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_loggedinuser_channel_name'),
        ('notifications', '0019_alter_notificationmanager_condition'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationmanager',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.organization'),
        ),
    ]
