from django import forms
from .models import Botines

class setBotinesForm(forms.ModelForm):
    class Meta:
        model = Botines
        fields = '__all__'

class BusquedaForm(forms.Form):
    termino_busqueda = forms.CharField(max_length=100)