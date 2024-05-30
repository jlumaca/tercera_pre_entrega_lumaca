from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context,loader
from AppCoder.models import Estudiante,Curso
#from django.db import connection
from AppCoder.forms import EstudianteFormulario

# Views principales
#################
def padre(req):
    return render(req,"padre.html")

def inicio(req):
    return render(req,"inicio.html")

def entregables(req):
    return render(req,"Entregables/entregables.html")

def profesores(req):
    return render(req,"Profesores/profesores.html")

def cursos(req):
    return render(req,"Cursos/cursos.html")

##########
def cursoForm(req):

    if req.method == 'POST':
            nuevo_curso = Curso(nombre = req.POST['nombreCurso'],comision = req.POST['comisionCurso'])
            nuevo_curso.save()
            return render(req, "cursos.html")
 
    return render(req,"cursos.html")

def buscarCurso(req):
   
        if req.GET['documentoEstudiante']:
            doc = req.GET['documentoEstudiante']
            estudiante = Estudiante.objects.filter(documento__icontains=doc)
            return render(req, "estudiantes.html", {"estudiante": estudiante})   
  
def buscarCursosTodos(req):
    
    if req.method == "GET":
        estudiantes = Curso.objects.all()
        return render(req, "cursos.html", {"cursos": estudiantes})


def estudianteForm(req):
 

  print('method: ', req.method)
  print('POST: ', req.POST)

  if req.method == 'POST':

    miFormulario = EstudianteFormulario(req.POST)

    if miFormulario.is_valid():

      informacion = miFormulario.cleaned_data

      nuevo_estudiante = Estudiante(documento = informacion['documento'],nombre = informacion['nombre'],apellido = informacion['apellido'],email = informacion['email'],telefono = informacion['telefono'])
      nuevo_estudiante.save()

      return render(req, "Estudiantes/estudiantes.html", {"message": "Estudiante ingresado con éxito"})
    
    else:

      return render(req, "Estudiantes/estudiantes.html", {"message": "Datos inválidos"})
  
  else:

    miFormulario = EstudianteFormulario()

    return render(req, "Estudiantes/estudiantes.html", {"miFormulario": miFormulario})

def buscarEstudianteX(req):

  if req.GET["documentoEstudiante"]:

    documento = req.GET["documentoEstudiante"]

    estudiante = Estudiante.objects.filter(documento__icontains=documento)

    return render(req, "Estudiantes/formConsultarEstudiante.html", {"estudiantes": estudiante, "documento": documento})

  else:
      
      return render(req, "Estudiantes/formConsultarEstudiante.html", {"message": "No envias el dato del estudiante"})

def buscarEstudiantesTodos(req):
    
    if req.method == "GET":
        estudiantes = Estudiante.objects.all()
        return render(req, "Estudiantes/formConsultarTodosEstudiantes.html", {"estudiantes": estudiantes})