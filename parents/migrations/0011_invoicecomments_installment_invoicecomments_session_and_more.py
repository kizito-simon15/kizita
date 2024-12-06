# Generated by Django 5.0.4 on 2024-07-06 03:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corecode', '0001_initial'),
        ('parents', '0010_parentcomments_exam'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicecomments',
            name='installment',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='corecode.installment'),
        ),
        migrations.AddField(
            model_name='invoicecomments',
            name='session',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='corecode.academicsession'),
        ),
        migrations.AddField(
            model_name='invoicecomments',
            name='term',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='corecode.academicterm'),
        ),
    ]
