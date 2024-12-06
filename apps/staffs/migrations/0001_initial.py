# Generated by Django 5.0.4 on 2024-06-18 12:52

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Staff",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "current_status",
                    models.CharField(
                        choices=[("active", "Active"), ("inactive", "Inactive")],
                        default="active",
                        max_length=10,
                    ),
                ),
                ("firstname", models.CharField(max_length=200)),
                ("middle_name", models.CharField(blank=True, max_length=200)),
                ("surname", models.CharField(max_length=200)),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "Male"), ("female", "Female")],
                        default="male",
                        max_length=10,
                    ),
                ),
                ("date_of_birth", models.DateField(default=django.utils.timezone.now)),
                (
                    "date_of_admission",
                    models.DateField(default=django.utils.timezone.now),
                ),
                (
                    "salary",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "mobile_number",
                    models.CharField(
                        blank=True,
                        max_length=13,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Entered mobile number isn't in the right format!",
                                regex="^[0-9]{10,15}$",
                            )
                        ],
                    ),
                ),
                (
                    "occupation",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("teacher", "Teacher"),
                            ("administrator", "Administrator"),
                            ("support_staff", "Support Staff"),
                            ("bursar", "Bursar"),
                            ("academic", "Academic"),
                            ("secretary", "Secretary"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                ("address", models.TextField(blank=True)),
                ("guarantor", models.CharField(blank=True, max_length=200)),
                ("contract_duration", models.CharField(blank=True, max_length=50)),
                ("nida_id", models.CharField(blank=True, max_length=20, null=True)),
                ("tin_number", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "contract_start_date",
                    models.DateField(default=django.utils.timezone.now),
                ),
                ("contract_end_date", models.DateField(blank=True, null=True)),
                (
                    "passport_photo",
                    models.ImageField(
                        blank=True, upload_to="students/passport_photos/"
                    ),
                ),
                ("others", models.TextField(blank=True)),
                (
                    "group",
                    models.CharField(
                        choices=[
                            ("teaching_staff", "Teaching Staff"),
                            ("non_teaching_staff", "Non Teaching Staff"),
                        ],
                        default="teaching_staff",
                        max_length=20,
                    ),
                ),
            ],
            options={
                "permissions": [
                    ("view_staff_list", "Can view staff list"),
                    ("view_staff_detail", "Can view staff details"),
                ],
            },
        ),
    ]