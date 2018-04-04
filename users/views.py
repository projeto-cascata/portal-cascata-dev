from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import UserProfile

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def profile(request):
    return render('user_profile.html', {})

def login(request):
    return render(request, 'login.html', {})
