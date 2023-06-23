from django.shortcuts import render
from AppWeb.forms import * 
from .models import Botines


# Create your views here.

def inicio(request):
    return render(request, "AppWeb/inicio.html")

def pelota(request):
    return render(request, "AppWeb/pelota.html")

def botines(request):
    return render(request, "AppWeb/botines.html")

def canilleras(request):
    return render(request, "AppWeb/canilleras.html")


def setBotines(request):
    
    if request.method == 'POST':
      
            botines =  Botines(request.post['marca'],(request.post['talle']))
 
            botines.save()
 
            return render(request, "AppWeb/inicio.html")
 
    return render(request, "AppWeb/setBotines.html")

   
def buscar(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['termino_busqueda']
            resultados = Botines.objects.filter(marca__icontains=termino_busqueda)
            return render(request, 'resultadosBusqueda.html', {'resultados': resultados})
    else:
        form = BusquedaForm()
    return render(request, 'buscar.html', {'form': form})