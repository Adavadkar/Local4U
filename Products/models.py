from django.db import models
from Home.models import Category
from LocalFarmers.models import Farmer



# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    farmer = models.ForeignKey(Farmer, related_name='products', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.name



