import json
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from django.core import serializers
from .models import Member
from .models import Student
from .models import DefaultUser
from .filters import MemberFilter
from .filters import StudentFilter

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def profile(request, user_id):

    user = DefaultUser.objects.get(enrollment=user_id)
    #user = Student.objects.get(enrollment=user_id)
    #user = Member.objects.get(enrollment=user_id)
    context = {
        'user': user,
    }
    return render(request, 'users/user_profile.html', context)


class MembersList(ListView):
    model = Member
    context_object_name = 'members'
    template_name = 'users/members_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        members = Member.objects.all()
        context['filter'] = MemberFilter(self.request.GET, queryset=members)
        return context


class StudentsList(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'users/students_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        students = Student.objects.all()
        context['filter'] = StudentFilter(self.request.GET, queryset=students)
        return context
