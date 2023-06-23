from django.db import models

# Create your models here.

class Botines(models.Model):
    marca = models.CharField(max_length=40)
    talle = models.IntegerField()

class Pelota(models.Model):
    marca = models.CharField(max_length=40)

class Canilleras(models.Model):
    marca = models.CharField(max_length=40)
