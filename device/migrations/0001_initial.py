# Generated by Django 4.0.1 on 2022-06-07 10:59

from django.db import migrations, models
import django.db.models.deletion
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, null=True, unique=True)),
                ('title', models.CharField(max_length=32)),
                ('default_unit', models.CharField(blank=True, max_length=32, null=True)),
                ('units', django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=8), blank=True, null=True, size=None)),
                ('value', models.CharField(choices=[('CONTINUES', 'CONTINUES'), ('BINARY', 'BINARY')], default='continues', max_length=10)),
            ],
            options={
                'db_table': 'type',
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_number', models.CharField(max_length=16, unique=True)),
                ('title', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('will_topic', models.CharField(max_length=128)),
                ('value_topic', models.CharField(db_index=True, max_length=128)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_online', models.BooleanField(default=False)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.organization')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.type')),
            ],
            options={
                'db_table': 'sensor',
                'ordering': ('part_number',),
            },
        ),
        migrations.CreateModel(
            name='Actuator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_number', models.CharField(max_length=16, unique=True)),
                ('title', models.CharField(default='', max_length=32, unique=True)),
                ('will_topic', models.CharField(max_length=128)),
                ('value_topic', models.CharField(db_index=True, max_length=128)),
                ('value', models.FloatField(blank=True, default=0)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_online', models.BooleanField(default=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.organization')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.type')),
            ],
            options={
                'db_table': 'actuator',
                'ordering': ('part_number',),
            },
        ),
        migrations.AddIndex(
            model_name='sensor',
            index=models.Index(fields=['part_number'], name='sensor_part_nu_f73d9a_idx'),
        ),
    ]