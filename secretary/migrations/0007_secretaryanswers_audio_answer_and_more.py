# Generated by Django 5.1.2 on 2024-11-01 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "secretary",
            "0006_rename_mark_secretary_comment_secretaryanswers_mark_secretary_answer",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="secretaryanswers",
            name="audio_answer",
            field=models.FileField(
                blank=True, null=True, upload_to="secretary_audio_answers/"
            ),
        ),
        migrations.AlterField(
            model_name="secretaryanswers",
            name="answer",
            field=models.TextField(blank=True),
        ),
    ]
