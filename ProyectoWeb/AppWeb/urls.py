from django.urls import path 
from AppWeb.views import *

urlpatterns = [
    path('inicio/', inicio, name = "Inicio"),
    path('pelota/' , pelota, name = "Pelota"),
    path('botines/', botines, name = "Botines"),
    path('canilleras/', canilleras, name = "Canilleras"),
    path('setBotines/',setBotines, name = "setBotines"),
    path('buscarBotines/', buscarBotines, name = "buscarBotines"),
    path('buscar/', buscar, name = "buscar"), 
]