from django.contrib import admin
from django.urls import path
from AppCoder import views
#from proyecto_django_lumaca.views import prueba

urlpatterns = [
    path('', views.padre,name="Padre"),#
    path('inicio', views.inicio,name="Inicio"),#
    path('estudiantes', views.estudianteForm,name="Estudiantes"),#
    path('cursos', views.cursoForm,name="Cursos"),#
    path('entregables', views.entregables,name="Entregables"),#
    path('profesores', views.profesores,name="Profesores"),#
    path('buscarEstudiante', views.buscarEstudianteX,name="BuscarEstudiante"),
    path('buscarEstudiantes', views.buscarEstudiantesTodos,name="BuscarEstudiantes"),
    #path('estudiantesForm', views.estudianteForm,name="FormEstudiantes"),#
    
    
    #path('cursosForm', views.cursoForm,name="Cursos"),
    path('buscarCursos', views.buscarCursosTodos,name="BuscarCursos"),
    path('buscarCurso', views.buscarCursoY,name="BuscarCurso"),
    #path('volverEstudiante', views.estudianteForm,name="Estudiante"),
    #path('formIngresarEstudiante', views.ingresarEstudiante,name="IngresarEstudiante"),
    #path('formConsultarEstudiante', views.buscarUnEstudiante,name="ConsultarEstudiante"),
    #path('formConsultarTodosEstudiantes', views.buscarEstudiantes,name="ConsultarEstudiantes")
]
