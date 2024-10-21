from http.client import HTTPResponse

from django.shortcuts import render

from Home.models import Category
from LocalFarmers.models import Farmer


# Create your views here.
def index(request):
    categories = Category.objects.all()
    farmers = Farmer.objects.all()
    return render(request, 'index.html', {'categories': categories, 'farmers': farmers})
