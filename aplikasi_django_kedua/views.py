from django.shortcuts import render
from .models import Product

def tes(request):
    products = Product.objects.first()
    return render(request, 'tes.html', {'products': products})