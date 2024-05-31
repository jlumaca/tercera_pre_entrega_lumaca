from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context,loader
from AppCoder.models import Estudiante,Curso,Profesor
#from django.db import connection
from AppCoder.forms import EstudianteFormulario,CursoFormulario, ProfesorFormulario

# Views principales
#################
def padre(req):
    return render(req,"padre.html")

def inicio(req):
    return render(req,"inicio.html")

def entregables(req):
    return render(req,"Entregables/entregables.html")




##########





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

def cursoForm(req):
    print('method: ', req.method)
    print('POST: ', req.POST)

    if req.method == 'POST':

        miFormulario = CursoFormulario(req.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            nuevo_curso = Curso(nombre = informacion['nombre'], comision = informacion['comision'])
            nuevo_curso.save()

            return render(req, "Cursos/cursos.html", {"message": "Curso ingresado con éxito"})
        
        else:

            return render(req, "Cursos/cursos.html", {"message": "Datos inválidos"})
    
    else:

        miFormulario = CursoFormulario()

        return render(req, "Cursos/cursos.html", {"miFormulario": miFormulario})
    


def buscarCursoY(req):
   
        if req.GET["comisionCurso"]:

            comision = req.GET["comisionCurso"]

            curso = Curso.objects.filter(comision__icontains=comision)

            return render(req, "Cursos/formConsultarCurso.html", {"cursos": curso, "comision": comision})

        else:
      
            return render(req, "Cursos/formConsultarCurso.html", {"message": "No envias el dato del curso"})  
  
def buscarCursosTodos(req):
    
    if req.method == "GET":
        estudiantes = Curso.objects.all()
        return render(req, "Cursos/formConsultarTodosCursos.html", {"cursos": estudiantes})

def profesorForm(req):
    print('method: ', req.method)
    print('POST: ', req.POST)

    if req.method == 'POST':

        miFormulario = ProfesorFormulario(req.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            nuevo_profesor = Profesor(documento = informacion['documento'],nombre = informacion['nombre'],apellido = informacion['apellido'],email = informacion['email'],telefono = informacion['telefono'],profesion = informacion['curso'])
            nuevo_profesor.save()

            return render(req, "Profesores/profesores.html", {"message": "Profesor ingresado con éxito"})
        
        else:

            return render(req, "Profesores/profesores.html", {"message": "Datos inválidos"})
    
    else:

        miFormulario = ProfesorFormulario()
        return render(req, "Profesores/profesores.html", {"miFormulario": miFormulario})

def buscarProfesorZ(req):
   
        if req.GET["documentoProfesor"]:

            documento = req.GET["documentoProfesor"]

            profesor = Profesor.objects.filter(documento__icontains=documento)

            return render(req, "Profesores/formConsultarProfesor.html", {"profesores": profesor, "documento": documento})

        else:
      
            return render(req, "Profesores/formConsultarProfesor.html", {"message": "No envias el dato del curso"})  
    

def buscarProfesoresTodos(req):
    
    if req.method == "GET":
        profesores = Profesor.objects.all()
        return render(req, "Profesores/formConsultarTodosProfesores.html", {"profesores": profesores})