# Generated by Django 5.1.2 on 2024-11-05 12:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("corecode", "0002_signature"),
        ("duty", "0002_alter_staffroles_subject"),
        ("staffs", "0007_staffattendance_date_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="DailySchedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "day",
                    models.CharField(
                        choices=[
                            ("Monday", "Monday"),
                            ("Tuesday", "Tuesday"),
                            ("Wednesday", "Wednesday"),
                            ("Thursday", "Thursday"),
                            ("Friday", "Friday"),
                            ("Saturday", "Saturday"),
                            ("Sunday", "Sunday"),
                        ],
                        max_length=20,
                        unique=True,
                    ),
                ),
                (
                    "start_time",
                    models.TimeField(help_text="Start time for school activities."),
                ),
                (
                    "end_time",
                    models.TimeField(help_text="End time for school activities."),
                ),
            ],
            options={
                "ordering": ["day"],
            },
        ),
        migrations.CreateModel(
            name="ClassSchedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
                (
                    "activity_type",
                    models.CharField(
                        choices=[
                            ("study", "Study"),
                            ("break", "Break"),
                            ("event", "Event"),
                        ],
                        default="study",
                        max_length=100,
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        help_text="Optional description for the activity (e.g., 'Morning Assembly')",
                        max_length=200,
                    ),
                ),
                (
                    "staff",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="class_staff",
                        to="staffs.staff",
                    ),
                ),
                (
                    "student_class",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="schedules",
                        to="corecode.studentclass",
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="class_subjects",
                        to="corecode.subject",
                    ),
                ),
                (
                    "daily_schedule",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="class_schedules",
                        to="duty.dailyschedule",
                    ),
                ),
            ],
            options={
                "ordering": ["daily_schedule__day", "student_class", "start_time"],
                "unique_together": {
                    ("daily_schedule", "student_class", "start_time", "end_time")
                },
            },
        ),
    ]