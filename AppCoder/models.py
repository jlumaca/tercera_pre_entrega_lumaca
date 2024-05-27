from django.db import models

# Create your models here.

class Estudiante(models.Model):
    documento = models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
