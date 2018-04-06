from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from users.models import User


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")