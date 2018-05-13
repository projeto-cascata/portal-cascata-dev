from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('', views.ListDisciplines.as_view(), name='disciplines'),
    path('add_material/<int:discipline_id>', views.MaterialView.as_view(), name='add-material')
]