from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.utils.decorators import method_decorator

from .forms import MaterialForm
from .models import Discipline, DisciplineComponent
from .models import Material


class ListDisciplines(ListView):
    model = Discipline
    template_name = "index.html"

class DetailDiscipline(DetailView):
    model = Discipline
    template_name = "discipline_detail.html"
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        user = self.request.user

        is_creator = user.has_perm('disciplines.add_material')
        context['is_creator'] = is_creator

        return context


decorators = [permission_required('disciplines.add_material', login_url='/disciplines/')]

@method_decorator(decorators, name='dispatch')
class MaterialView(View):
    form_class = MaterialForm
    template_name = 'add_material.html'
    previous_page = ''

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

            return HttpResponseRedirect('/disciplines/')
        
        context = {
            'form': form,
            'discipline': discipline,
        }
        return render(request, self.template_name, context=context)