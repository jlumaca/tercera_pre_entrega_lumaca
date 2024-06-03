from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context,loader
from AppCoder.models import Estudiante,Curso,Profesor,Entregable
#from django.db import connection
from AppCoder.forms import EstudianteFormulario,CursoFormulario, ProfesorFormulario,EntregableFormulario

# Views principales
#################
def padre(req):
    return render(req,"padre.html")

def inicio(req):
    return render(req,"inicio.html",{'active_page': 'inicio'})

def existePersona(documento):
    estudiante = Estudiante.objects.filter(documento__icontains=documento)

    if estudiante:
        return True
    else:
        return False

def existeCurso(comision):
    curso = Curso.objects.filter(comision__icontains=comision)

    if curso:
        return True
    else:
        return False

def estudianteForm(req):
 

  print('method: ', req.method)
  print('POST: ', req.POST)

  if req.method == 'POST':

    miFormulario = EstudianteFormulario(req.POST)

    if miFormulario.is_valid():

      informacion = miFormulario.cleaned_data
      if existePersona(informacion['documento']):
        return render(req, "Estudiantes/estudiantes.html", {"message": "Estudiante ya existe",'active_page': 'estudiantes'})
      else:
        nuevo_estudiante = Estudiante(documento = informacion['documento'],nombre = informacion['nombre'],apellido = informacion['apellido'],email = informacion['email'],telefono = informacion['telefono'])
        nuevo_estudiante.save()

        return render(req, "Estudiantes/estudiantes.html", {"message": "Estudiante ingresado con éxito",'active_page': 'estudiantes'})
    
    else:

      return render(req, "Estudiantes/estudiantes.html", {"message": "Datos inválidos",'active_page': 'estudiantes'})
  
  else:

    miFormulario = EstudianteFormulario()

    return render(req, "Estudiantes/estudiantes.html", {"miFormulario": miFormulario,'active_page': 'estudiantes'})

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
            if existeCurso(informacion['comision']):
                return render(req, "Cursos/cursos.html", {"message": "Curso con esta comisión ya existe",'active_page': 'cursos'})
            else:
                nuevo_curso = Curso(nombre = informacion['nombre'], comision = informacion['comision'])
                nuevo_curso.save()

                return render(req, "Cursos/cursos.html", {"message": "Curso ingresado con éxito",'active_page': 'cursos'})
        
        else:

            return render(req, "Cursos/cursos.html", {"message": "Datos inválidos",'active_page': 'cursos'})
    
    else:

        miFormulario = CursoFormulario()

        return render(req, "Cursos/cursos.html", {"miFormulario": miFormulario,'active_page': 'cursos'})
    


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
            if existePersona(informacion['documento']):
                return render(req, "Profesores/profesores.html", {"message": "Profesor ya existe",'active_page': 'profesores'})
            else:
                nuevo_profesor = Profesor(documento = informacion['documento'],nombre = informacion['nombre'],apellido = informacion['apellido'],email = informacion['email'],telefono = informacion['telefono'],profesion = informacion['curso'])
                nuevo_profesor.save()

                return render(req, "Profesores/profesores.html", {"message": "Profesor ingresado con éxito",'active_page': 'profesores'})
        
        else:

            return render(req, "Profesores/profesores.html", {"message": "Datos inválidos",'active_page': 'profesores'})
    
    else:

        miFormulario = ProfesorFormulario()
        return render(req, "Profesores/profesores.html", {"miFormulario": miFormulario,'active_page': 'profesores'})

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


def entregablesForm(req):
    print('method: ', req.method)
    print('POST: ', req.POST)

    if req.method == 'POST':

        miFormulario = EntregableFormulario(req.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            nuevo_entregable = Entregable(nombre = informacion['nombre'],fecha_entrega = informacion['fecha_de_entrega'],entregado = informacion['entregado'])
            nuevo_entregable.save()

            return render(req, "Entregables/entregables.html", {"message": "Entregable ingresado con éxito",'active_page': 'entregables'})
        
        else:

            return render(req, "Entregables/entregables.html", {"message": "Datos inválidos",'active_page': 'entregables'})
    
    else:

        miFormulario = EntregableFormulario()
        return render(req, "Entregables/entregables.html", {"miFormulario": miFormulario,'active_page': 'entregables'})

def buscarEntregableW(req):
   
        if req.GET["fecha_entregable"]:

            fecha_entrega = req.GET["fecha_entregable"]

            entregables = Entregable.objects.filter(fecha_entrega__icontains=fecha_entrega)
            
            for entregable in entregables:
                if entregable.entregado:
                    entregable.entregado = "Entregado"
                else:
                    entregable.entregado = "NO entregado"

            return render(req, "Entregables/formConsultarEntregable.html", {"entregables": entregables, "fecha_entrega": fecha_entrega})

        else:
      
            return render(req, "Entregables/formConsultarEntregable.html", {"message": "No envias el dato del entregable"})  
    

def buscarEntregablesTodos(req):
    
    if req.method == "GET":
        entregables = Entregable.objects.all()
        return render(req, "Entregables/formConsultarTodosEntregables.html", {"entregables": entregables})
    