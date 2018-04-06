from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:user_id>', views.profile),
    url('login', views.login),
]
