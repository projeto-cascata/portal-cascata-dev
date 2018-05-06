from django.urls import path
from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    path('profile/<int:user_id>/', views.profile),
    path('members_list/', views.MembersList.as_view(), name='members_list'),
    path('students_list/', views.StudentsList.as_view(), name='students_list'),
]
