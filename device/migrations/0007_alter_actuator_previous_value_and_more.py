# Generated by Django 4.0.1 on 2022-08-25 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0006_alter_actuator_set_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actuator',
            name='previous_value',
            field=models.FloatField(blank=True, choices=[(0, 'off'), (1, 'on')], default=0),
        ),
        migrations.AlterField(
            model_name='actuator',
            name='set_value',
            field=models.FloatField(blank=True, choices=[(0, 'off'), (1, 'on')], default=0),
        ),
        migrations.AlterField(
            model_name='actuator',
            name='value',
            field=models.FloatField(blank=True, choices=[(0, 'off'), (1, 'on')], default=0),
        ),
    ]
