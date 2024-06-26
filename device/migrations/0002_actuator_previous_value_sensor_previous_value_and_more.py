# Generated by Django 4.0.1 on 2022-06-22 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actuator',
            name='previous_value',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='sensor',
            name='previous_value',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='sensor',
            name='value',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
