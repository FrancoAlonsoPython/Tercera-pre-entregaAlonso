from django import forms

class setBotinesform(forms.Form):
    marca = forms.CharField(max_length=30)
    talle = forms.IntegerField(max_value=30) 
    

