from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class InfoExtraUsuario(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	#additional
	telefono = models.IntegerField(blank = False)

	def __str__(self):
		return self.user.username