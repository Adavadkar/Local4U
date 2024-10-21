# Generated by Django 5.1.1 on 2024-10-21 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Home', '0002_rename_farmers_name_category_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=255)),
                ('categories', models.ManyToManyField(related_name='farmers', to='Home.category')),
            ],
        ),
    ]
