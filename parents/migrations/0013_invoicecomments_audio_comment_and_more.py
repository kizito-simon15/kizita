# Generated by Django 5.1.2 on 2024-11-01 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("parents", "0012_remove_invoicecomments_term"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoicecomments",
            name="audio_comment",
            field=models.FileField(
                blank=True, null=True, upload_to="invoice_audio_comments/"
            ),
        ),
        migrations.AddField(
            model_name="parentcomments",
            name="audio_comment",
            field=models.FileField(
                blank=True, null=True, upload_to="parent_audio_comments/"
            ),
        ),
        migrations.AddField(
            model_name="studentcomments",
            name="audio_comment",
            field=models.FileField(
                blank=True, null=True, upload_to="student_audio_comments/"
            ),
        ),
        migrations.AlterField(
            model_name="invoicecomments",
            name="comment",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="parentcomments",
            name="comment",
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="studentcomments",
            name="comment",
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
