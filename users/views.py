from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
from django.core import serializers


from .models import Member

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def profile(request, user_id):
    user = Member.objects.get(enrollment=user_id)
    context = {
        'user': user,
    }
    return render(request, 'users/user_profile.html', context)

def members_list(request):
    members = Member.objects.all()

    membersJSON = []
    for member in members: 
        membersJSON.append(member.get_json())

    return render(request, 'users/members_list.html', {'members': members, 'members_json': membersJSON})
