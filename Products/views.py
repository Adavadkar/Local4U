from django.shortcuts import render
from Products.models import Product

# View to display all products
def product_list(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'Products/product_list.html', {'products': products})

# View to display products by category
def products_by_category(request, category_id):
    products = Product.objects.filter(category_id=category_id)  # Fetch products by category
    return render(request, 'products/products_by_category.html', {'products': products})

