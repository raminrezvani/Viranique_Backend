# Generated by Django 4.0.1 on 2022-07-30 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0005_automatictile_alarm_manualtile_alarm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manualtile',
            name='alarm',
        ),
    ]