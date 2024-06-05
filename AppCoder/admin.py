from django.contrib import admin
from .models import *

# REGISTRO DE MODELS PARA /admin

admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Entregable)
admin.site.register(Profesor)