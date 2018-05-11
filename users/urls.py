from django.urls import path
from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    path('profile/<int:user_id>/', views.profile),
    url(r'^members_list/$', views.members_list),
    url(r'^invite_students/$', views.invite_students),
]
