from django.contrib import admin

from Products.models import Product
from .models import Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)

