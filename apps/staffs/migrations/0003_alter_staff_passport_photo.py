# Generated by Django 5.0.4 on 2024-08-19 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0002_remove_staff_group_alter_staff_mobile_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='passport_photo',
            field=models.ImageField(blank=True, upload_to='students/'),
        ),
    ]