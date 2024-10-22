from django.contrib import admin

from LocalFarmers.models import Farmer
from Products.models import Product
from .models import Category

# Register your models here.
#admin.site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
admin.site.register(Farmer)

