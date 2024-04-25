# Generated by Django 4.0.1 on 2022-06-26 05:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_remove_organization_notification_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoggedInUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='logged_in_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
