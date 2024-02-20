from django.shortcuts import render, redirect
from .models import Product, Coba
from .forms import ProductForm

def tes(request):
    products = Product.objects.all()
    coba = Coba.objects.first()
    last = Coba.objects.last()
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()  # Save data to database
            return redirect('kedua:tes')
    else:
        form = ProductForm()
    
    return render(request, 'tes.html', {'form': form, 'products': products, 'coba': coba, 'last': last})
