# Generated by Django 5.0.6 on 2024-09-01 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_age_profile_has_insurance_benefit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='session_replay_url',
            field=models.URLField(null=True),
        ),
    ]
