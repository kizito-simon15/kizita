# Generated by Django 4.2.16 on 2024-11-10 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0003_meeting_is_past'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='meeting_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
