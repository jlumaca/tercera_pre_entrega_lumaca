from django.http import HttpResponse
from django.template import Template, Context

def prueba(req):
    miHtml = open("D:/tercera_pre_entrega_lumaca/mi_proyecto_lumaca/mi_proyecto_lumaca/templates/template1.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)