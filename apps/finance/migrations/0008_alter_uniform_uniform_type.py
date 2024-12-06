# Generated by Django 5.0.4 on 2024-07-26 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0007_studentuniform_uniform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uniform',
            name='uniform_type',
            field=models.CharField(choices=[('SHATI', 'Shati'), ('SKETI/KAPTULA', 'Sketi/Kaptula'), ('SWETA', 'Sweta'), ('SOKSI', 'Soksi'), ('T-SHIRT', 'T-Shirt'), ('KAPTULA YA MICHEZO', 'Kaptula ya Michezo'), ('FULL_UNIFORM', 'Full Uniform')], max_length=20),
        ),
    ]
