# Generated by Django 5.0.4 on 2024-06-26 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0007_customuser_language"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="language",
            field=models.CharField(
                choices=[
                    ("en", "English"),
                    ("es", "Spanish"),
                    ("fr", "French"),
                    ("sw", "Kiswahili"),
                ],
                default="en",
                max_length=10,
            ),
        ),
    ]
