from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Person
# Create your views here.


class PersonsListView(ListView):
    model = Person
    template_name = 'person/person_list.html'
    context_object_name = 'persons'


class PersonDetailView(DetailView):
    model = Person
    template_name = 'person/person_detail.html'
    context_object_name = 'person'

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data['relateds'] = Person.objects.filter(anime=data['person'].anime)
        return data 
