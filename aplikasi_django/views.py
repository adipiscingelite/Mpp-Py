from django.shortcuts import render
from django.http import HttpResponse

def coba(request):
    return HttpResponse("Hello world!")
  # return render(request, 'index.html')

def home(request):
    return HttpResponse("ini home")
  # return render(request, 'index.html')

