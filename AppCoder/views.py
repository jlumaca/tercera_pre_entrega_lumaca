from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context,loader
from AppCoder.models import Estudiante,Curso,Profesor,Entregable
from django.db import OperationalError, IntegrityError
#from django.db import connection
from AppCoder.forms import EstudianteFormulario,CursoFormulario, ProfesorFormulario,EntregableFormulario

# Views principales
#################
#def padre(req):
#    return render(req,"padre.html")

def inicio(req):
    return render(req,"inicio.html",{'active_page': 'inicio'})

def existePersona(documento,que_persona):
   
    estudiante = Estudiante.objects.filter(documento=documento)
    profesor = Profesor.objects.filter(documento=documento)
        
    if que_persona == "Est":
        if estudiante.exists():
            return True
        else:
            return False
    else:
        if profesor.exists():
            return True
        else:
            return False

def existeCurso(comision):
    curso = Curso.objects.filter(comision=comision)

    if curso.exists():
        return True
    else:
        return False

def estudianteForm(req):
 
    try:
        print('method: ', req.method)
        print('POST: ', req.POST)

        if req.method == 'POST':

            miFormulario = EstudianteFormulario(req.POST)

            if miFormulario.is_valid():

                informacion = miFormulario.cleaned_data
                if existePersona(informacion['documento'],"Est"):
                    return render(req, "Estudiantes/estudiantes.html", {"error_message": "Estudiante ya existe",'active_page': 'estudiantes'})
                else:
                    nuevo_estudiante = Estudiante(documento = informacion['documento'],nombre = informacion['nombre'],apellido = informacion['apellido'],email = informacion['email'],telefono = informacion['telefono'])
                    nuevo_estudiante.save()

                    return render(req, "Estudiantes/estudiantes.html", {"message": "Estudiante ingresado con éxito",'active_page': 'estudiantes'})
                
            else:
                return render(req, "Estudiantes/estudiantes.html", {"error_message": "Datos inválidos",'active_page': 'estudiantes'})
        
        else:

            miFormulario = EstudianteFormulario()

            return render(req, "Estudiantes/estudiantes.html", {"miFormulario": miFormulario,'active_page': 'estudiantes'})
    except OperationalError as e:
    # Manejar errores operativos de la base de datos
        return render(req, "Estudiantes/estudiantes.html", {'error_message':f"Ha ocurrido un error no controlado con la base de datos: {str(e)}",'active_page': 'estudiantes'})
    except IntegrityError as e:
    # Manejar errores de integridad de la base de datos
        return render(req, "Estudiantes/estudiantes.html", {'error_message':f"Ha ocurrido un error de integridad no controlado con la base de datos: {str(e)}",'active_page': 'estudiantes'})
    except ValueError as e:
    # Manejar errores de valor, por ejemplo, si 'documento' es None
        return render(req, "Estudiantes/estudiantes.html", {'error_message':f"Se deben ingresar los datos: {str(e)}",'active_page': 'estudiantes'})
    except Exception as e:
    # Manejar cualquier otra excepción no prevista
        return render(req, "Estudiantes/estudiantes.html", {'error_message':f"Excepción no controlada: {str(e)}",'active_page': 'estudiantes'})

def buscarEstudianteX(req):
    try:
        if req.GET["documentoEstudiante"]:

            documento = req.GET["documentoEstudiante"]

            estudiante = Estudiante.objects.filter(documento=documento)

            return render(req, "Estudiantes/formConsultarEstudiante.html", {"estudiantes": estudiante, "documento": documento,'active_page': 'estudiantes'})

        else:
            
            return render(req, "Estudiantes/formConsultarEstudiante.html", {"error_message": "No envias el dato del estudiante",'active_page': 'estudiantes'})
    except OperationalError as e:
    # Manejar errores operativos de la base de datos
        return render(req, "Estudiantes/formConsultarEstudiante.html", {'error_message':f"Ha ocurrido un error no controlado con la base de datos: {str(e)}",'active_page': 'estudiantes'})
    except IntegrityError as e:
    # Manejar errores de integridad de la base de datos
        return render(req, "Estudiantes/formConsultarEstudiante.html", {'error_message':f"Ha ocurrido un error de integridad no controlado con la base de datos: {str(e)}",'active_page': 'estudiantes'})
    except ValueError as e:
    # Manejar errores de valor, por ejemplo, si 'documento' es None
        return render(req, "Estudiantes/formConsultarEstudiante.html", {'error_message':f"Se deben ingresar los datos: {str(e)}",'active_page': 'estudiantes'})
    except Exception as e:
    # Manejar cualquier otra excepción no prevista
        return render(req, "Estudiantes/formConsultarEstudiante.html", {'error_message':f"Excepción no controlada: {str(e)}",'active_page': 'estudiantes'})
def buscarEstudiantesTodos(req):
    try:
        if req.method == "GET":
            estudiantes = Estudiante.objects.all()
            return render(req, "Estudiantes/formConsultarTodosEstudiantes.html", {"estudiantes": estudiantes,'active_page': 'estudiantes'})
    except OperationalError as e:
    # Manejar errores operativos de la base de datos
        return render(req, "Estudiantes/formConsultarTodosEstudiantes.html", {'error_message':f"Ha ocurrido un error no controlado con la base de datos: {str(e)}",'active_page': 'estudiantes'})
    except IntegrityError as e:
    # Manejar errores de integridad de la base de datos
        return render(req, "Estudiantes/formConsultarTodosEstudiantes.html", {'error_message':f"Ha ocurrido un error de integridad no controlado con la base de datos: {str(e)}",'active_page': 'estudiantes'})
    except ValueError as e:
    # Manejar errores de valor, por ejemplo, si 'documento' es None
        return render(req, "Estudiantes/formConsultarTodosEstudiantes.html", {'error_message':f"Se deben ingresar los datos: {str(e)}",'active_page': 'estudiantes'})
    except Exception as e:
    # Manejar cualquier otra excepción no prevista
        return render(req, "Estudiantes/formConsultarTodosEstudiantes.html", {'error_message':f"Excepción no controlada: {str(e)}",'active_page': 'estudiantes'})
def cursoForm(req):
        try:
            print('method: ', req.method)
            print('POST: ', req.POST)

            if req.method == 'POST':

                miFormulario = CursoFormulario(req.POST)

                if miFormulario.is_valid():

                    informacion = miFormulario.cleaned_data
                    if existeCurso(informacion['comision']):
                        return render(req, "Cursos/cursos.html", {"error_message": "Curso con esta comisión ya existe",'active_page': 'cursos'})
                    else:
                        nuevo_curso = Curso(nombre = informacion['nombre'], comision = informacion['comision'])
                        nuevo_curso.save()

                        return render(req, "Cursos/cursos.html", {"message": "Curso ingresado con éxito",'active_page': 'cursos'})
                
                else:

                    return render(req, "Cursos/cursos.html", {"error_message": "Datos inválidos",'active_page': 'cursos'})
            
            else:

                miFormulario = CursoFormulario()

                return render(req, "Cursos/cursos.html", {"miFormulario": miFormulario,'active_page': 'cursos'})
        except OperationalError as e:
    # Manejar errores operativos de la base de datos
            return render(req, "Cursos/cursos.html", {'error_message':f"Ha ocurrido un error no controlado con la base de datos: {str(e)}",'active_page': 'cursos'})
        except IntegrityError as e:
    # Manejar errores de integridad de la base de datos
            return render(req, "Cursos/cursos.html", {'error_message':f"Ha ocurrido un error de integridad no controlado con la base de datos: {str(e)}",'active_page': 'cursos'})
        except ValueError as e:
    # Manejar errores de valor, por ejemplo, si 'documento' es None
            return render(req, "Cursos/cursos.html", {'error_message':f"Se deben ingresar los datos: {str(e)}",'active_page': 'cursos'})
        except Exception as e:
    # Manejar cualquier otra excepción no prevista
            return render(req, "Cursos/cursos.html", {'error_message':f"Excepción no controlada: {str(e)}",'active_page': 'cursos'})


def buscarCursoY(req):
    try:
        if req.GET["comisionCurso"]:

            comision = req.GET["comisionCurso"]

            curso = Curso.objects.filter(comision=comision)

            return render(req, "Cursos/formConsultarCurso.html", {"cursos": curso, "comision": comision,'active_page': 'cursos'})

        else:
      
            return render(req, "Cursos/formConsultarCurso.html", {"error_message": "No envias el dato del curso",'active_page': 'cursos'})  
    except OperationalError as e:
    # Manejar errores operativos de la base de datos
        return render(req, "Cursos/formConsultarCurso.html", {'error_message':f"Ha ocurrido un error no controlado con la base de datos: {str(e)}",'active_page': 'cursos'})
    except IntegrityError as e:
    # Manejar errores de integridad de la base de datos
        return render(req, "Cursos/formConsultarCurso.html", {'error_message':f"Ha ocurrido un error de integridad no controlado con la base de datos: {str(e)}",'active_page': 'cursos'})
    except ValueError as e:
    # Manejar errores de valor, por ejemplo, si 'documento' es None
        return render(req, "Cursos/formConsultarCurso.html", {'error_message':f"Se deben ingresar los datos: {str(e)}",'active_page': 'cursos'})
    except Exception as e:
    # Manejar cualquier otra excepción no prevista
        return render(req, "Cursos/formConsultarCurso.html", {'error_message':f"Excepción no controlada: {str(e)}",'active_page': 'cursos'})
def buscarCursosTodos(req):
    try:
        if req.method == "GET":
            estudiantes = Curso.objects.all()
            return render(req, "Cursos/formConsultarTodosCursos.html", {"cursos": estudiantes,'active_page': 'cursos'})
    
    except OperationalError as e:
    # Manejar errores operativos de la base de datos
        return render(req, "Cursos/formConsultarTodosCursos.html", {'error_message':f"Ha ocurrido un error no controlado con la base de datos: {str(e)}",'active_page': 'cursos'})
    except IntegrityError as e:
    # Manejar errores de integridad de la base de datos
        return render(req, "Cursos/formConsultarTodosCursos.html", {'error_message':f"Ha ocurrido un error de integridad no controlado con la base de datos: {str(e)}",'active_page': 'cursos'})
    except ValueError as e:
    # Manejar errores de valor, por ejemplo, si 'documento' es None
        return render(req, "Cursos/formConsultarTodosCursos.html", {'error_message':f"Se deben ingresar los datos: {str(e)}",'active_page': 'cursos'})
    except Exception as e:
    # Manejar cualquier otra excepción no prevista
        return render(req, "Cursos/formConsultarTodosCursos.html", {'error_message':f"Excepción no controlada: {str(e)}",'active_page': 'cursos'})

def profesorForm(req):
    try:    
        print('method: ', req.method)
        print('POST: ', req.POST)

        if req.method == 'POST':

            miFormulario = ProfesorFormulario(req.POST)

            if miFormulario.is_valid():

                informacion = miFormulario.cleaned_data
                if existePersona(informacion['documento'],"Prof"):
                    return render(req, "Profesores/profesores.html", {"error_message": "Profesor ya existe",'active_page': 'profesores'})
                else:
                    nuevo_profesor = Profesor(documento = informacion['documento'],nombre = informacion['nombre'],apellido = informacion['apellido'],email = informacion['email'],telefono = informacion['telefono'],profesion = informacion['curso'])
                    nuevo_profesor.save()

                    return render(req, "Profesores/profesores.html", {"message": "Profesor ingresado con éxito",'active_page': 'profesores'})
            
            else:

                return render(req, "Profesores/profesores.html", {"error_message": "Datos inválidos",'active_page': 'profesores'})
        
        else:

            miFormulario = ProfesorFormulario()
            return render(req, "Profesores/profesores.html", {"miFormulario": miFormulario,'active_page': 'profesores'})
    except OperationalError as e:
    # Manejar errores operativos de la base de datos
        return render(req, "Profesores/profesores.html", {'error_message':f"Ha ocurrido un error no controlado con la base de datos: {str(e)}",'active_page': 'profesores'})
    except IntegrityError as e:
    # Manejar errores de integridad de la base de datos
        return render(req, "Profesores/profesores.html", {'error_message':f"Ha ocurrido un error de integridad no controlado con la base de datos: {str(e)}",'active_page': 'profesores'})
    except ValueError as e:
    # Manejar errores de valor, por ejemplo, si 'documento' es None
        return render(req, "Profesores/profesores.html", {'error_message':f"Se deben ingresar los datos: {str(e)}",'active_page': 'profesores'})
    except Exception as e:
    # Manejar cualquier otra excepción no prevista
        return render(req, "Profesores/profesores.html", {'error_message':f"Excepción no controlada: {str(e)}",'active_page': 'profesores'})

def buscarProfesorZ(req):
    try:
        if req.GET["documentoProfesor"]:

            documento = req.GET["documentoProfesor"]

            profesor = Profesor.objects.filter(documento=documento)

            return render(req, "Profesores/formConsultarProfesor.html", {"profesores": profesor, "documento": documento,'active_page': 'profesores'})

        else:
      
            return render(req, "Profesores/formConsultarProfesor.html", {"error_message": "No envias el dato del curso",'active_page': 'profesores'})
    except OperationalError as e:
    # Manejar errores operativos de la base de datos
        return render(req, "Profesores/formConsultarProfesor.html", {'error_message':f"Ha ocurrido un error no controlado con la base de datos: {str(e)}",'active_page': 'profesores'})
    except IntegrityError as e:
    # Manejar errores de integridad de la base de datos
        return render(req, "Profesores/formConsultarProfesor.html", {'error_message':f"Ha ocurrido un error de integridad no controlado con la base de datos: {str(e)}",'active_page': 'profesores'})
    except ValueError as e:
    # Manejar errores de valor, por ejemplo, si 'documento' es None
        return render(req, "Profesores/formConsultarProfesor.html", {'error_message':f"Se deben ingresar los datos: {str(e)}",'active_page': 'profesores'})
    except Exception as e:
    # Manejar cualquier otra excepción no prevista
        return render(req, "Profesores/formConsultarProfesor.html", {'error_message':f"Excepción no controlada: {str(e)}",'active_page': 'profesores'})
    

def buscarProfesoresTodos(req):
    try:
        if req.method == "GET":
            profesores = Profesor.objects.all()
            return render(req, "Profesores/formConsultarTodosProfesores.html", {"profesores": profesores,'active_page': 'profesores'})
    except OperationalError as e:
    # Manejar errores operativos de la base de datos
        return render(req, "Profesores/formConsultarTodosProfesores.html", {'error_message':f"Ha ocurrido un error no controlado con la base de datos: {str(e)}",'active_page': 'profesores'})
    except IntegrityError as e:
    # Manejar errores de integridad de la base de datos
        return render(req, "Profesores/formConsultarTodosProfesores.html", {'error_message':f"Ha ocurrido un error de integridad no controlado con la base de datos: {str(e)}",'active_page': 'profesores'})
    except ValueError as e:
    # Manejar errores de valor, por ejemplo, si 'documento' es None
        return render(req, "Profesores/formConsultarTodosProfesores.html", {'error_message':f"Se deben ingresar los datos: {str(e)}",'active_page': 'profesores'})
    except Exception as e:
    # Manejar cualquier otra excepción no prevista
        return render(req, "Profesores/formConsultarTodosProfesores.html", {'error_message':f"Excepción no controlada: {str(e)}",'active_page': 'profesores'})

def entregablesForm(req):
    try:
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

                return render(req, "Entregables/entregables.html", {"error_message": "Datos inválidos",'active_page': 'entregables'})
        
        else:

            miFormulario = EntregableFormulario()
            return render(req, "Entregables/entregables.html", {"miFormulario": miFormulario,'active_page': 'entregables'})
    except OperationalError as e:
    # Manejar errores operativos de la base de datos
        return render(req, "Entregables/entregables.html", {'error_message':f"Ha ocurrido un error no controlado con la base de datos: {str(e)}",'active_page': 'entregables'})
    except IntegrityError as e:
    # Manejar errores de integridad de la base de datos
        return render(req, "Entregables/entregables.html", {'error_message':f"Ha ocurrido un error de integridad no controlado con la base de datos: {str(e)}",'active_page': 'entregables'})
    except ValueError as e:
    # Manejar errores de valor, por ejemplo, si 'documento' es None
        return render(req, "Entregables/entregables.html", {'error_message':f"Se deben ingresar los datos: {str(e)}",'active_page': 'entregables'})
    except Exception as e:
    # Manejar cualquier otra excepción no prevista
        return render(req, "Entregables/entregables.html", {'error_message':f"Excepción no controlada: {str(e)}",'active_page': 'entregables'})

def buscarEntregableW(req):
    try:
        if req.GET["fecha_entregable"]:

            fecha_entrega = req.GET["fecha_entregable"]

            entregables = Entregable.objects.filter(fecha_entrega=fecha_entrega)
            
            for entregable in entregables:
                if entregable.entregado:
                    entregable.entregado = "Corregido"
                else:
                    entregable.entregado = "No corregido"

            return render(req, "Entregables/formConsultarEntregable.html", {"entregables": entregables, "fecha_entrega": fecha_entrega,'active_page': 'entregables'})

        else:
      
            return render(req, "Entregables/formConsultarEntregable.html", {"error_message": "No envias el dato del entregable",'active_page': 'entregables'})  
    except OperationalError as e:
    # Manejar errores operativos de la base de datos
        return render(req, "Entregables/formConsultarEntregable.html", {'error_message':f"Ha ocurrido un error no controlado con la base de datos: {str(e)}",'active_page': 'entregables'})
    except IntegrityError as e:
    # Manejar errores de integridad de la base de datos
        return render(req, "Entregables/formConsultarEntregable.html", {'error_message':f"Ha ocurrido un error de integridad no controlado con la base de datos: {str(e)}",'active_page': 'entregables'})
    except ValueError as e:
    # Manejar errores de valor, por ejemplo, si 'documento' es None
        return render(req, "Entregables/formConsultarEntregable.html", {'error_message':f"Se deben ingresar los datos: {str(e)}",'active_page': 'entregables'})
    except Exception as e:
    # Manejar cualquier otra excepción no prevista
        return render(req, "Entregables/formConsultarEntregable.html", {'error_message':f"Excepción no controlada: {str(e)}",'active_page': 'entregables'})

def buscarEntregablesTodos(req):
    try:
        if req.method == "GET":
            entregables = Entregable.objects.all()
            for entregable in entregables:
                    if entregable.entregado:
                        entregable.entregado = "Corregido"
                    else:
                        entregable.entregado = "No corregido"
            return render(req, "Entregables/formConsultarTodosEntregables.html", {"entregables": entregables,'active_page': 'entregables'})
    except OperationalError as e:
    # Manejar errores operativos de la base de datos
        return render(req, "Entregables/formConsultarTodosEntregables.html", {'error_message':f"Ha ocurrido un error no controlado con la base de datos: {str(e)}",'active_page': 'entregables'})
    except IntegrityError as e:
    # Manejar errores de integridad de la base de datos
        return render(req, "Entregables/formConsultarTodosEntregables.html", {'error_message':f"Ha ocurrido un error de integridad no controlado con la base de datos: {str(e)}",'active_page': 'entregables'})
    except ValueError as e:
    # Manejar errores de valor, por ejemplo, si 'documento' es None
        return render(req, "Entregables/formConsultarTodosEntregables.html", {'error_message':f"Se deben ingresar los datos: {str(e)}",'active_page': 'entregables'})
    except Exception as e:
    # Manejar cualquier otra excepción no prevista
        return render(req, "Entregables/formConsultarTodosEntregables.html", {'error_message':f"Excepción no controlada: {str(e)}",'active_page': 'entregables'})