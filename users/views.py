from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def login(request):
    template = loader.get_template('login.html')
    return render(request, 'login.html', {})

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
