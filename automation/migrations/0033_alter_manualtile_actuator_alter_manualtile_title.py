# Generated by Django 4.0.1 on 2022-09-28 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0007_alter_actuator_previous_value_and_more'),
        ('automation', '0032_remove_manualtile_unique_manual_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manualtile',
            name='actuator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='device.actuator', unique=True),
        ),
        migrations.AlterField(
            model_name='manualtile',
            name='title',
            field=models.CharField(default='', max_length=24, unique=True),
        ),
    ]