from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context,loader
# Create your views here.
def inicio(req):
    return render(req,"padre.html")


def estudiantes(req):
    return render(req,"estudiantes.html")

def entregables(req):
    return render(req,"entregables.html")

def profesores(req):
    return render(req,"profesores.html")

def cursos(req):
    return render(req,"cursos.html")