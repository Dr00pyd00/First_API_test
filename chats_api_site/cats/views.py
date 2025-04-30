from django.shortcuts import render
from django.views.generic import CreateView,UpdateView, DetailView,DeleteView, ListView
from .models import Cat
from django.urls import reverse_lazy


# Create your views here.


class CatList(ListView):
    model = Cat
    context_object_name = 'cats'
    
    
class CatDetail(DetailView):
    model = Cat
    context_object_name = 'cat'
        

class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')
    

class CatDelete(DeleteView):
    model = Cat
    success_url = reverse_lazy('cats:cat_list')
    

class CatUpdate(UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')
    


    