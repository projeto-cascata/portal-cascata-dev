from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user
from users.models import Member
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required

from .forms import NewsForm

# Create your views here.
def index(request):
    return HttpResponse('<h1> News Index </h1>')

@permission_required('news.add_newsitem', login_url='/news/index/')
def create_news(request):
    if request.method == 'GET':
        form = NewsForm()
        context = {'form': form}
        print(form.data)
        return render(request, 'create_news.html', context) 
    
    elif request.method == 'POST' and request.user.is_authenticated:
        form = NewsForm(request.POST)

        print(request.POST)
        print(form.data)

        if form.is_valid():
            post = form.save(commit=False)
            
            logged_user = get_user(request)
            member_account = Member.objects.get(email = logged_user.email)

            post.posted_by = member_account
            post.save()
            return HttpResponseRedirect('/news/index/')
    else:
        return HttpResponse('Unauthorized', status=401)