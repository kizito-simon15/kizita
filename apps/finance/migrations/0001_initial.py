# Generated by Django 5.0.4 on 2024-06-18 12:52

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("corecode", "0001_initial"),
        ("staffs", "0001_initial"),
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Invoice",
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
                ("balance_from_previous_install", models.IntegerField(default=0)),
                (
                    "status",
                    models.CharField(
                        choices=[("active", "Active"), ("closed", "Closed")],
                        default="active",
                        max_length=20,
                    ),
                ),
                (
                    "class_for",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="corecode.studentclass",
                    ),
                ),
                (
                    "installment",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="corecode.installment",
                    ),
                ),
                (
                    "session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="corecode.academicsession",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="students.student",
                    ),
                ),
            ],
            options={
                "ordering": ["student", "installment"],
            },
        ),
        migrations.CreateModel(
            name="InvoiceItem",
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
                ("description", models.CharField(max_length=200)),
                ("amount", models.IntegerField()),
                (
                    "invoice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="finance.invoice",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Receipt",
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
                ("amount_paid", models.IntegerField()),
                ("date_paid", models.DateField(default=django.utils.timezone.now)),
                ("comment", models.CharField(blank=True, max_length=200)),
                (
                    "payment_method",
                    models.CharField(
                        choices=[
                            ("NMB_BANK", "NMB BANK"),
                            ("M_PESA", "M-PESA"),
                            ("CASH", "CASH"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "invoice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="finance.invoice",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SalaryInvoice",
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
                ("month", models.DateField(default=django.utils.timezone.now)),
                ("gross_salary", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "deductions",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "net_salary",
                    models.DecimalField(
                        decimal_places=2, editable=False, max_digits=10
                    ),
                ),
                ("issued_date", models.DateField(default=django.utils.timezone.now)),
                ("remarks", models.TextField(blank=True)),
                (
                    "staff",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="staffs.staff"
                    ),
                ),
            ],
        ),
    ]