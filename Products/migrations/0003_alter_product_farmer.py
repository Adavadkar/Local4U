# Generated by Django 5.1.1 on 2024-10-21 15:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_farmer_alter_product_price_product_farmer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='farmer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.farmer'),
        ),
    ]
