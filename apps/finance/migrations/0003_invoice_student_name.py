# Generated by Django 5.0.4 on 2024-07-03 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("finance", "0002_alter_invoice_student"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="student_name",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]