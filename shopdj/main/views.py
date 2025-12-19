from django.shortcuts import render
from django.http import HttpResponse

def base(request):
    context ={
        'title': 'Base Page',
        'content': 'Best Shop Page',
    }
    return render(request, 'main/base.html', context)

def index(request):
    context ={
        'title': 'Home Page',
        'content': 'Best Shop Page',
    }
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse("About Page")

