from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user
from users.models import DefaultUser
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

        return render(request, 'create_news.html', context) 
    
    elif request.method == 'POST' and request.user.is_authenticated:
        form = NewsForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            
            user = get_user(request)
            default_user = DefaultUser.objects.get(email = user.email)

            post.posted_by = default_user
            post.save()
            return HttpResponseRedirect('/news/index/')
    else:
        return HttpResponse('Unauthorized', status=401)