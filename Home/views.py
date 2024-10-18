from http.client import HTTPResponse

from django.shortcuts import render

from Home.models import Category


# Create your views here.
def index(request):
    cat1 = Category()
    cat2 = Category()
    cat3 = Category()
    cat4 = Category()
    cat5 = Category()
    cat6 = Category()
    cat7 = Category()
    cat1.name = 'Fruits and Vegetables'
    cat2.name = 'Baked Goods'
    cat3.name = 'Ready to Eat Foods'
    cat4.name = 'Organic Meat'
    cat5.name = 'Soups'
    cat6.name = 'Organic Dairy products'

    context = {
        'cat1': cat1,
        'cat2': cat2,
        'cat3': cat3,
        'cat4': cat4,
        'cat5': cat5,
        'cat6': cat6,
    }

    return render(request, 'index.html', context)
