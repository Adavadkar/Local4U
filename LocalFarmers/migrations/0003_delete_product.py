# Generated by Django 5.1.1 on 2024-10-22 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LocalFarmers', '0002_remove_farmer_categories_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]