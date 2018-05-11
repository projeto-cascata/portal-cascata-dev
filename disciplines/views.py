from django.shortcuts import render
from .models import Discipline
from django.views.generic import ListView

class ListDisciplines(ListView):
    model = Discipline
    template_name = "index.html"