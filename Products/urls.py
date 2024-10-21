from django import urls
from django.urls import path

from Home.urls import urlpatterns
from . import views

urlpatterns = [
    path('category/<str:category_name>/', views.products_by_category, name='products_by_category'),
]