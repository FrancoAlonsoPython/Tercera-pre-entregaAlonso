from django import forms

class BuscarBotinesform(forms.Form):
    marca = forms.CharField(max_length=30)
    talle = forms.IntegerField(max_value=50) 
    

