from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('create_news/', views.create_news, name='create_news'),
    path('index/', views.index, name='news_index'),
    path('news_list/', views.NewsList.as_view(), name='news_list'),
    path('news_detail/', views.news_detail),
]