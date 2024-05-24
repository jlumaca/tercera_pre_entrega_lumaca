from django.contrib import admin
from django.urls import path
from AppCoder import views
#from proyecto_django_lumaca.views import prueba

urlpatterns = [
    path('', views.inicio,name="Inicio"),
    path('entregables', views.entregables,name="Entregables"),
    path('profesores', views.profesores,name="Profesores"),
    path('cursos', views.cursos,name="Cursos"),
    path('estudiantes', views.estudiantes,name="Estudiantes")
]
