# Generated by Django 5.1.2 on 2024-11-04 12:45

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("corecode", "0002_signature"),
        ("staffs", "0007_staffattendance_date_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="StaffRoles",
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
                ("is_class_teacher", models.BooleanField(default=False)),
                ("on_duty", models.BooleanField(default=False)),
                ("date_assigned", models.DateField(default=django.utils.timezone.now)),
                (
                    "assigned_class",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="class_roles",
                        to="corecode.studentclass",
                    ),
                ),
                (
                    "staff",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="roles",
                        to="staffs.staff",
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subject_roles",
                        to="corecode.subject",
                    ),
                ),
            ],
            options={
                "verbose_name": "Staff Role",
                "verbose_name_plural": "Staff Roles",
                "unique_together": {("staff", "assigned_class", "subject")},
            },
        ),
    ]
