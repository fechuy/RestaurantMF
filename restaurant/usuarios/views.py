from usuarios.forms import UserForm, UserAdminForm, InfoExtraUsuarioForm
from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, FormView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . import models
# Create your views here.

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))

def registro(request):
	registered = False
	
	if request.method == "POST":
		user_form = UserForm(data=request.POST)
		profile_form = InfoExtraUsuarioForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			profile.save()

			registered = True

		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = InfoExtraUsuarioForm()

	return render(request, 'usuarios/registro.html', 
					{'user_form':user_form,
					'profile_form':profile_form,
					'registered':registered})

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))

			else:
				return HttpResponse("Cuenta no activa")
		else:
			print("Error al iniciar sesion")
			print("Usuario: {} and pass {}".format(username,password))
			return HttpResponse("Login invalido")
	else:
		return render(request, 'usuarios/login.html', {})