# Generated by Django 4.0.1 on 2024-02-06 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0007_alter_tile_precision'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tile',
            name='size',
            field=models.CharField(choices=[('small', 'small'), ('medium', 'medium'), ('large', 'large'), ('Xlarge', 'Xlarge')], max_length=8),
        ),
    ]
