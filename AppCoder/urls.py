from django.contrib import admin
from django.urls import path
from AppCoder import views


urlpatterns = [
    path('', views.inicio,name="Inicio"),#
    path('estudiantes', views.estudianteForm,name="Estudiantes"),#ESTUDIANTES
    path('buscarEstudiante', views.buscarEstudianteX,name="BuscarEstudiante"),#ESTUDIANTES
    path('buscarEstudiantes', views.buscarEstudiantesTodos,name="BuscarEstudiantes"),#ESTUDIANTES
    path('cursos', views.cursoForm,name="Cursos"),#CURSOS
    path('buscarCursos', views.buscarCursosTodos,name="BuscarCursos"),#CURSOS
    path('buscarCurso', views.buscarCursoY,name="BuscarCurso"),#CURSOS
    path('profesores', views.profesorForm,name="Profesores"),#PROFESORES
    path('buscarProfesor', views.buscarProfesorZ,name="BuscarProfesor"),#PROFESORES
    path('buscarProfesores', views.buscarProfesoresTodos,name="BuscarProfesores"),#PROFESORES
    path('entregables', views.entregablesForm,name="Entregables"),#ENTREGABLES
    path('buscarEntregables', views.buscarEntregablesTodos,name="BuscarEntregables"),#ENTREGABLES
    path('buscarEntregable', views.buscarEntregableW,name="BuscarEntregable"),#ENTREGABLES
]
