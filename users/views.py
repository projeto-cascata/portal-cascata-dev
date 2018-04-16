from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import DefaultUser

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def profile(request, user_id):
    user = DefaultUser.objects.get(enrollment=user_id)
    context = {
        'user': user,
    }
    return render(request, 'users/user_profile.html', context)

def members_list(request):
    return render(request, 'users/members_list.html', {})
