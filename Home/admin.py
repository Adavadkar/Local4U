from django.contrib import admin

from LocalFarmers.models import Farmer
from Products.models import Product
from .models import Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Farmer)

