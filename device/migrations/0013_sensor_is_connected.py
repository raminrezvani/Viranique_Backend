# Generated by Django 4.0.1 on 2022-12-31 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0012_sensor_will_alt_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='is_connected',
            field=models.BooleanField(default=False),
        ),
    ]