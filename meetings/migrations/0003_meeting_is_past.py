# Generated by Django 5.1.2 on 2024-11-07 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meetings", "0002_agenda"),
    ]

    operations = [
        migrations.AddField(
            model_name="meeting",
            name="is_past",
            field=models.BooleanField(default=False),
        ),
    ]
