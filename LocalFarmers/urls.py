from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('products/category/<int:category_id>/', views.products_by_category, name='products_by_category'),
    # Add the farmer filtering URL if it's not already there:
    path('products/farmer/<int:farmer_id>/', views.products_by_farmer, name='products_by_farmer'),
]
