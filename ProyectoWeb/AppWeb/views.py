from django.shortcuts import render
from AppWeb.forms import *
from .models import Botines
from django.http import HttpResponse

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
        botine = Botines(marca=request.POST["marca"],talle=request.POST["talle"] )
        botine.save()
        return render(request,"AppWeb/inicio.html")

    return render(request, "AppWeb/setBotines.html")


   
def buscarBotines(request):
    return render(request, "AppWeb/buscarBotines.html")
  

#def buscar(request):
#    if request.GET["marca"]:
#        marca = request.GET["marca"]
#        botines = Botines.objects.filter(marca = marca)
#        return render(request, "AppWeb/buscarBotines.html", {"Botines":botines})
#    else:
#        respuesta = "No se enviaron datos"
#    
#    return HttpResponse(respuesta)

def buscar(request):
    form = BuscarBotinesform()

    if request.GET.get("marca"):
        marca = request.GET["marca"]
        botines = Botines.objects.filter(marca=marca)
        return render(request, "AppWeb/buscarBotines.html", {"botines": botines, "form": form})

    return render(request, "AppWeb/buscarBotines.html", {"form": form})