from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user
from users.models import Member
from news.models import NewsItem
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.views.generic.list import ListView
from django.utils import timezone

from .forms import NewsForm
from .models import NewsItem

# Create your views here.
def index(request):
    return HttpResponse('<h1> News Index </h1>')

def list_news(request):
    return render(request, 'news/news_list.html')

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

class NewsList(ListView):
    model = NewsItem

    context_object_name = 'news'
    template_name = 'news_list.html'
    #paginate_by = 50  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
        
def news_detail(request):
    news = NewsItem.objects.all()
    context = {
        'news': news,
    }
    return render(request, 'news_detail.html', context)
