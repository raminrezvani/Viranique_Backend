# Generated by Django 4.0.1 on 2022-08-04 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condition', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='continuescondition',
            name='set_point',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
