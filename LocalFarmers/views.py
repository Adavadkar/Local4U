from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import (Farmer)
from Products.models import Product
from Home.models import Category

# View to display products by category
def products_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'products_by_category.html', {'products': products, 'category': category})

# View to display products by farmer
def products_by_farmer(request, farmer_id):
    farmer = get_object_or_404(Farmer, id=farmer_id)
    products = Product.objects.filter(farmer=farmer)
    return render(request, 'products_by_farmer.html', {'products': products, 'farmer': farmer})

