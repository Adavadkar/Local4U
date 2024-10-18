from django.db import models
from Home.models import Category


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.ForeignKey(Category,related_name='products', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


