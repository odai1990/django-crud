from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Snack
from django.urls import reverse_lazy

# Create your views here.
class SnacksView(ListView):
    template_name='SnackListView.html'
    model=Snack


class SnacksDetials(DetailView):
    template_name='SnackDetailView.html'
    model=Snack

class SnacksCreate(CreateView):
    template_name='SnackCreateView.html'
    model=Snack
    fields=['title','purchaser','description']


class SnacksUpdate(UpdateView):
    template_name='SnackUpdateView.html'
    model=Snack
    fields=['title','purchaser','description']

class SnacksDelete(DeleteView):
    template_name='SnackDeleteView.html'
    model=Snack
    success_url=reverse_lazy('snackslist')
    
    