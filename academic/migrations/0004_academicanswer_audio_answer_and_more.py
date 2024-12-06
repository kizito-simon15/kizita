# Generated by Django 5.1.2 on 2024-11-01 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("academic", "0003_academicanswer_mark_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="academicanswer",
            name="audio_answer",
            field=models.FileField(
                blank=True, null=True, upload_to="academic_audio_answers/"
            ),
        ),
        migrations.AlterField(
            model_name="academicanswer",
            name="answer",
            field=models.TextField(blank=True),
        ),
    ]