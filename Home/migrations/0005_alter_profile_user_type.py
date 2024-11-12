# Generated by Django 5.1.1 on 2024-11-11 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[('farmer', 'Farmer'), ('customer', 'Customer'), ('admin', 'Admin'), ('vendor', 'Vendor')], max_length=10),
        ),
    ]