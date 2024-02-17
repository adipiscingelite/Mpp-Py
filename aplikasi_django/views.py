from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello world!")
    return render(request, 'index.html')
  

def home(request):
    return render(request, 'home.html')

# def index_kedua(request):
#     return render(request, 'kedua/home.html')

# # cek