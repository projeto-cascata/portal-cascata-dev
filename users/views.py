from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.template import loader

from .models import UserProfile

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def profile(request):
    template = loader.get_template('user_profile.html')
    context = {

    }
    return HttpResponse(template.render(context, request))