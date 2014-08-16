from django import forms
from aerolinea.models import Cliente, Vuelo, Pasaje


class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente

class VueloForm(forms.ModelForm):
	class Meta:
		model = Vuelo
			
class PasajeForm(forms.ModelForm):
	class Meta:
		model = Pasaje
		
			

