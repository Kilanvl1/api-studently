# Generated by Django 5.0.6 on 2024-10-10 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_profile_is_lead'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_lead',
        ),
    ]
