from django.db import models

# MODELS CON SUS RESPECTIVAS COLUMNAS

class Estudiante(models.Model):
    documento = models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)



class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    comision = models.IntegerField()

class Profesor(models.Model):
    documento = models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    profesion = models.CharField(max_length=30)

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()
