from django.contrib import admin
from django.urls import path
from AppCoder import views
#from proyecto_django_lumaca.views import prueba

urlpatterns = [
    path('', views.padre,name="Padre"),
    path('inicio', views.inicio,name="Inicio"),
    path('entregables', views.entregables,name="Entregables"),
    path('profesores', views.profesores,name="Profesores"),
    path('cursos', views.cursos,name="Cursos"),
    path('estudiantes', views.estudiantes,name="Estudiantes"),
    path('estudiantesForm', views.estudianteForm,name="FormEstudiantes"),
    path('buscarEstudiantes', views.buscarEstudiantesTodos,name="BuscarEstudiantes"),
    path('buscarEstudiante', views.buscarEstudiante,name="BuscarEstudiante"),
    path('formIngresarEstudiante', views.ingresarEstudiante,name="IngresarEstudiante"),
    path('formConsultarEstudiante', views.buscarUnEstudiante,name="ConsultarEstudiante"),
    path('formConsultarTodosEstudiantes', views.buscarEstudiantes,name="ConsultarEstudiantes")
]
