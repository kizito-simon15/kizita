# Generated by Django 5.0.4 on 2024-06-21 15:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_parentuser_parent_middle_name"),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("staffs", "0001_initial"),
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("username", models.CharField(max_length=10, unique=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.RemoveField(
            model_name="parentuser",
            name="groups",
        ),
        migrations.RemoveField(
            model_name="parentuser",
            name="id",
        ),
        migrations.RemoveField(
            model_name="parentuser",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="parentuser",
            name="is_staff",
        ),
        migrations.RemoveField(
            model_name="parentuser",
            name="is_superuser",
        ),
        migrations.RemoveField(
            model_name="parentuser",
            name="last_login",
        ),
        migrations.RemoveField(
            model_name="parentuser",
            name="password",
        ),
        migrations.RemoveField(
            model_name="parentuser",
            name="user_permissions",
        ),
        migrations.RemoveField(
            model_name="parentuser",
            name="username",
        ),
        migrations.AlterField(
            model_name="parentuser",
            name="student",
            field=models.OneToOneField(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="students.student",
            ),
        ),
        migrations.AddField(
            model_name="parentuser",
            name="customuser_ptr",
            field=models.OneToOneField(
                auto_created=True,
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="AcademicUser",
            fields=[
                (
                    "customuser_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "staff",
                    models.OneToOneField(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="staffs.staff",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("accounts.customuser",),
        ),
        migrations.CreateModel(
            name="BursorUser",
            fields=[
                (
                    "customuser_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "staff",
                    models.OneToOneField(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="staffs.staff",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("accounts.customuser",),
        ),
        migrations.CreateModel(
            name="SecretaryUser",
            fields=[
                (
                    "customuser_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "staff",
                    models.OneToOneField(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="staffs.staff",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("accounts.customuser",),
        ),
        migrations.CreateModel(
            name="TeacherUser",
            fields=[
                (
                    "customuser_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "staff",
                    models.OneToOneField(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="staffs.staff",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("accounts.customuser",),
        ),
    ]
