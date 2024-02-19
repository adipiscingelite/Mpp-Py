from django.shortcuts import render
from .models import Product, Coba

def tes(request):
    products = Product.objects.all()
    coba = Coba.objects.first()
    last = Coba.objects.last()
    return render(request, 'tes.html', {'products': products, 'coba': coba, 'last': last})