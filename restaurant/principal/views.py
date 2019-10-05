from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, UpdateView, DeleteView, CreateView

# Create your views here.

class IndexView(TemplateView):
	template_name = 'principal/index.html'

class reservacionTemplateView(TemplateView):
	template_name = 'principal/reservacion.html'