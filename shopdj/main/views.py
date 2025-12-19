from django.shortcuts import render
from django.http import HttpResponse

def index(request):
          
    context ={
        'title': 'home',
        'content':'welcome to the home page',
        'list': [1,2,3],
        'gor': 'Just',
        'user': False,
    }
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse("About Page")

