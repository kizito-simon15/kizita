# Generated by Django 5.0.4 on 2024-06-23 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("parents", "0005_invoicecomments_date_commented_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoicecomments",
            name="satisfied",
            field=models.BooleanField(default=False),
        ),
    ]
