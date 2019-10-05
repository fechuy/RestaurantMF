from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, FormView

# Create your views here.

class menuTemplateView(TemplateView):
	template_name = 'productos/menu.html'