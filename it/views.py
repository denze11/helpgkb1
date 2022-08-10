from django.views.generic import ListView, CreateView, UpdateView
from .forms import ItForm, EditItForm
from django.shortcuts import render
from . models import ItYear


class ItView(ListView):
    model = ItYear
    template_name = 'it_tasks.html'

    # Список начинается с последнего
    ordering = ['-date_created']


class AddItView(CreateView):
    model = ItYear
    form_class = ItForm
    template_name = 'it.html'


class UpdateItView(UpdateView):
    model = ItYear
    form_class = EditItForm
    template_name = 'it_update.html'
    #fields = ['performer', 'completed', 'date_completed']
