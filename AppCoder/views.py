from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context,loader
from AppCoder.models import Estudiante
from AppCoder.forms import EstudianteFormulario

# Create your views here.
def padre(req):
    return render(req,"padre.html")

def inicio(req):
    return render(req,"inicio.html")


def estudiantes(req):
    return render(req,"estudiantes.html")

def entregables(req):
    return render(req,"entregables.html")

def profesores(req):
    return render(req,"profesores.html")

def cursos(req):
    return render(req,"cursos.html")


def formEstudiantes(req):
    return render(req,"estudiantes.html")

def estudianteForm(req):

    if req.method == 'POST':
            nuevo_estudiante = Estudiante(documento = req.POST['documentoEstudiante'],nombre = req.POST['nombreEstudiante'],apellido = req.POST['apellidoEstudiante'],email = req.POST['emailEstudiante'],telefono = req.POST['telefonoEstudiante'])
            nuevo_estudiante.save()
            return render(req, "estudiantes.html")
 
    return render(req,"estudiantes.html")
