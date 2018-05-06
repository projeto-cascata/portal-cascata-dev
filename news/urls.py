from django.urls import path

from . import views

urlpatterns = [
    path('create_news/', views.create_news),
    path('index/', views.index),

]