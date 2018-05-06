from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
from django.core import serializers
from .models import Member
from .models import Student
from .filters import MemberFilter
from .filters import StudentFilter

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
    member_filter = MemberFilter(request.GET, queryset=members)
    return render(request, 'users/members_list.html', { 'members': members, 'filter': member_filter})
    
def students_list(request):
    students = Student.objects.all()
    student_filter = StudentFilter(request.GET, queryset=students)
    return render(request, 'users/students_list.html', { 'students': students, 'filter': student_filter})
