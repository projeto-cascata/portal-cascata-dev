from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from users.models import User

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def profile(request, user_id):
    user = User.objects.get(enrollment=user_id)
    context = {
        'user': user,
    }
    print(user)
    return render(request, 'user_profile.html', context)