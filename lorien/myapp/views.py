from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Product

def test_page(request):
    items = Product.objects.all()
    context = {
        'items': items
    }
    return render(request, 'myapp/test_page.html', context)

def id_item(request, my_id):
    item = Product.objects.get(id = my_id)
    context = {
        'item': item
    }
    return render(request, 'myapp/detail.html', context = context)

