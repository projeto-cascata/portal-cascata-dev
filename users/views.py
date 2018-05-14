import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic import ListView
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Member
from .models import Student
from .models import DefaultUser
from .filters import MemberFilter
from .filters import StudentFilter
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    form = EmailForm()
    return render(request, 'users/invite_student.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/users/login')

def profile(request, user_id):

    user = None
    #user = Student.objects.get(enrollment=user_id)
    #user = Member.objects.get(enrollment=user_id)
    try:
        user = Member.objects.get(enrollment=user_id)
    except ObjectDoesNotExist:
        user = Student.objects.get(enrollment=user_id)
    context = {
        'user': user,
    }
    return render(request, 'users/user_profile.html', context)

@login_required
def own_profile(request):
    user = request.user
    try:
        user = Member.objects.get(email=user.email)
    except ObjectDoesNotExist:
        user = Student.objects.get(email=user.email)

    context = {
        'user': user
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

def invite_students(request):
+    form = EmailForm()
+    if request.method == 'POST':
+        form = EmailForm(request.POST)
+        if form.is_valid():
+            form_cleaned = form.cleaned_data
+            email = form_cleaned['email']
+            invite = Invitation.create(email, inviter=request.user)
+            invite.send_invitation(request)
