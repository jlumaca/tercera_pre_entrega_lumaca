from django.contrib import admin
from django.urls import path
from AppCoder import views
#from proyecto_django_lumaca.views import prueba

urlpatterns = [
    path('', views.padre,name="Padre"),#
    path('inicio', views.inicio,name="Inicio"),#
    path('estudiantes', views.estudianteForm,name="Estudiantes"),#ESTUDIANTES
    path('buscarEstudiante', views.buscarEstudianteX,name="BuscarEstudiante"),#ESTUDIANTES
    path('buscarEstudiantes', views.buscarEstudiantesTodos,name="BuscarEstudiantes"),#ESTUDIANTES
    path('cursos', views.cursoForm,name="Cursos"),#CURSOS
    path('buscarCursos', views.buscarCursosTodos,name="BuscarCursos"),#CURSOS
    path('buscarCurso', views.buscarCursoY,name="BuscarCurso"),#CURSOS
    path('profesores', views.profesorForm,name="Profesores"),#PROFESORES
    path('buscarProfesor', views.buscarProfesorZ,name="BuscarProfesor"),#PROFESORES
    path('buscarProfesores', views.buscarProfesoresTodos,name="BuscarProfesores"),#PROFESORES
    path('entregables', views.entregables,name="Entregables"),#ENTREGABLES
    #path('estudiantesForm', views.estudianteForm,name="FormEstudiantes"),#
    
    
    #path('cursosForm', views.cursoForm,name="Cursos"),
        #path('volverEstudiante', views.estudianteForm,name="Estudiante"),
    #path('formIngresarEstudiante', views.ingresarEstudiante,name="IngresarEstudiante"),
    #path('formConsultarEstudiante', views.buscarUnEstudiante,name="ConsultarEstudiante"),
    #path('formConsultarTodosEstudiantes', views.buscarEstudiantes,name="ConsultarEstudiantes")
]
