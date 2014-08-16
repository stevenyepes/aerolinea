from django import forms
from aerolinea.models import Cliente, Vuelo


class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente

class VueloForm(forms.ModelForm):
	class Meta:
		model = Vuelo
			
		

