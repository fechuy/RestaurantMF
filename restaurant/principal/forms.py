from django import forms
from principal.models import Reservaciones

class reservacionesForm(forms.ModelForm):
	
	class Meta:
		model = Reservaciones
		fields=('fecha_reservacion', 'hora_reservacion', 'num_personas', 'nombre_reservacion', 'telefono_reservacion', 'correo_reservacion')
