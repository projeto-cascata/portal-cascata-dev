from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import EmailForm
from django.apps import Invitation


from .models import DefaultUser

def index(request):
    form = EmailForm()
    return render(request, 'users/invite_student.html', {'form': form})

def profile(request, user_id):
    user = DefaultUser.objects.get(enrollment=user_id)
    context = {
        'user': user,
    }
    return render(request, 'users/user_profile.html', context)

def members_list(request):
    return render(request, 'users/members_list.html', {})

def invite_students(request):
    form = EmailForm()
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form_cleaned = form.cleaned_data
            email = form_cleaned['email']
            invite = Invitation.create(email, inviter=request.user)
            invite.send_invitation(request)