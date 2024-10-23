# Generated by Django 5.1.1 on 2024-10-22 06:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LocalFarmers', '0003_delete_product'),
        ('Products', '0003_alter_product_farmer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='farmer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='LocalFarmers.farmer', null=True),
        ),
        migrations.DeleteModel(
            name='Farmer',
        ),
    ]
