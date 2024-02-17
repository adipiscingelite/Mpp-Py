from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello world!")
    return render(request, 'index.html')
  

def blog(request):
    return render(request, 'blog.html')

# def index_kedua(request):
#     return render(request, 'kedua/home.html')

# # cek