# Generated by Django 4.0.1 on 2022-10-16 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0003_tile_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='tile',
            name='interval',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
