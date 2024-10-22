from django.db import models
from Home.models import Category

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name




