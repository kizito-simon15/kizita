# Generated by Django 5.0.4 on 2024-07-02 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="parent_first_name",
        ),
        migrations.RemoveField(
            model_name="student",
            name="parent_last_name",
        ),
        migrations.RemoveField(
            model_name="student",
            name="parent_middle_name",
        ),
        migrations.RemoveField(
            model_name="student",
            name="parent_student_id",
        ),
        migrations.AddField(
            model_name="student",
            name="archive_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="student",
            name="archived",
            field=models.BooleanField(default=False),
        ),
    ]
