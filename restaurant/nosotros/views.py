from usuarios.forms import UserForm, UserAdminForm, InfoExtraUsuarioForm
from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, FormView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . import models

# Create your views here.

class nosotosTemplateView(TemplateView):
		template_name = 'nosotros/contact.html'

class acercaTemplateView(TemplateView):
	template_name = 'nosotros/us.html'
		