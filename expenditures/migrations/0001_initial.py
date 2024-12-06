# Generated by Django 5.0.4 on 2024-06-18 12:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="ExpenditureInvoice",
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
                    "initial_balance",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                ("date", models.DateField()),
                ("depositor_name", models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name="Expenditure",
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
                ("item_name", models.CharField(max_length=100)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date", models.DateField()),
                ("description", models.TextField(blank=True, null=True)),
                ("quantity", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "attachment",
                    models.FileField(blank=True, null=True, upload_to="attachments/"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="expenditures.category",
                    ),
                ),
            ],
        ),
    ]