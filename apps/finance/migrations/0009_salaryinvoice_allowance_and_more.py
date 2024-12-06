# Generated by Django 5.0.4 on 2024-08-03 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0008_alter_uniform_uniform_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='salaryinvoice',
            name='allowance',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='salaryinvoice',
            name='total_given_salary',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10),
            preserve_default=False,
        ),
    ]
