from django.http import HttpResponse
from django.template import Template, Context,loader

def prueba(req):
    #CARGADOR DE TEMPLATE
    plantilla = loader.get_template("template1.html")
    documento = plantilla.render()

    return HttpResponse(documento)