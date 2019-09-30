from django import forms
from django.contrib.auth.models import User
from usuarios.models import InfoExtraUsuario
from django.contrib import admin
from django.forms import ModelForm

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")

	class Meta():
		model = User
		fields = ('first_name','last_name','username','email','password')

class UserAdminForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")

	class Meta():
		model = User
		fields = ('first_name','last_name','username','email','password','is_staff')

class InfoExtraUsuarioForm(forms.ModelForm):
	telefono = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'number'}), min_value=0)
	class Meta():
		model = InfoExtraUsuario
		fields = ('telefono',)