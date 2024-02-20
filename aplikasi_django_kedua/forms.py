# forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']
        labels = {
            'name': 'Nama Produk',
            'price': 'Harga'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan nama produk'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan harga produk'})
        }