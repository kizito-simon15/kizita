# Generated by Django 5.0.4 on 2024-08-22 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corecode', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('signature_image', models.ImageField(upload_to='signatures/')),
            ],
        ),
    ]
