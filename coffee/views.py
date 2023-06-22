from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Coffee


class CoffeeListView(ListView):
    template_name = "coffee/coffee-list.html"
    model = Coffee  


class CoffeeDetailView(DetailView):
    template_name = "coffee/coffee-detail.html"
    model = Coffee


class CoffeeCreateView(CreateView):
    template_name = "coffee/coffee-create.html"
    model = Coffee
    fields = ['name', 'price', 'desc', 'purchaser']
    success_url = reverse_lazy("coffee_list")


class CoffeeUpdateView(UpdateView):
    template_name = "coffee/coffee-update.html"
    model = Coffee
    fields = ['name', 'price', 'desc', 'purchaser']


class CoffeeDeleteView(DeleteView):
    template_name = "coffee/coffee-delete.html"
    model = Coffee
    success_url = reverse_lazy("coffee_list")