from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from .forms import MaterialForm
from .models import Discipline, DisciplineComponent
from .models import Material


class ListDisciplines(ListView):
    model = Discipline
    template_name = "index.html"

class DetailDiscipline(DetailView):
    model = Discipline
    template_name = "discipline_detail.html"

class MaterialView(View):
    form_class = MaterialForm
    template_name = 'add_material.html'

    def get(self, request, discipline_id):
        form = self.form_class()
        discipline = DisciplineComponent.objects.get(pk=discipline_id)

        context = {
            'form': form,
            'discipline': discipline,
        }
        return render(request, self.template_name, context=context)

    def post(self, request, discipline_id):
        form = self.form_class(request.POST, request.FILES)
        discipline = DisciplineComponent.objects.get(pk=discipline_id)

        if form.is_valid():
            post = form.save(commit=False)

            post.discipline = discipline
            post.save()

            # Redirects to last page visited before the creation page.
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
        
        context = {
            'form': form,
            'discipline': discipline,
        }
        return render(request, self.template_name, context=context)