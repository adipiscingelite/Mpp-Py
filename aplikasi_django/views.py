from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    context = {
        'firstname': 'Linus',
        'lastname': 'Ardianto',
    }
    return render(request, 'index.html', context)
    # return HttpResponse("Hello world!")

def blog(request):
    return render(request, 'blog.html')