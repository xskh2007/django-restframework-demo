# Generated by Django 3.0.6 on 2020-06-08 02:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_delete',
        ),
        migrations.AlterField(
            model_name='user',
            name='user_secret',
            field=models.UUIDField(default=uuid.UUID('d79b52de-f528-4284-ad1b-e35e2c2c4465'), help_text='user secret'),
        ),
    ]