# Generated by Django 5.0.4 on 2024-08-26 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0008_alter_schoollocation_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoollocation',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='schoollocation',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='schoollocation',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True),
        ),
    ]
