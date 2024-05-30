from django.contrib import admin
from django.urls import path
from AppCoder import views
#from proyecto_django_lumaca.views import prueba

urlpatterns = [
    path('', views.padre,name="Padre"),#
    path('inicio', views.inicio,name="Inicio"),#
    path('entregables', views.entregables,name="Entregables"),#
    path('profesores', views.profesores,name="Profesores"),#
    path('cursos', views.cursos,name="Cursos"),#
    path('estudiantes', views.estudianteForm,name="Estudiantes"),#
    #path('estudiantesForm', views.estudianteForm,name="FormEstudiantes"),#
    path('buscarEstudiantes', views.buscarEstudiantesTodos,name="BuscarEstudiantes"),
    path('buscarEstudiante', views.buscarEstudianteX,name="BuscarEstudiante"),
    path('cursosForm', views.cursoForm,name="FormCursos"),
    path('buscarCursos', views.buscarCursosTodos,name="BuscarCursos"),
    #path('buscarCurso', views.buscarEstudiante,name=""),
    path('volverEstudiante', views.estudianteForm,name="Estudiante"),
    #path('formIngresarEstudiante', views.ingresarEstudiante,name="IngresarEstudiante"),
    #path('formConsultarEstudiante', views.buscarUnEstudiante,name="ConsultarEstudiante"),
    #path('formConsultarTodosEstudiantes', views.buscarEstudiantes,name="ConsultarEstudiantes")
]
