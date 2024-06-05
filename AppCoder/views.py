from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context,loader
from AppCoder.models import Estudiante,Curso,Profesor,Entregable
from django.db import OperationalError, IntegrityError
from AppCoder.forms import EstudianteFormulario,CursoFormulario, ProfesorFormulario,EntregableFormulario

#FUNCIONES DE VALIDACION DE INGRESO DE DATOS, SI EXISTE EL MISMO RETORNA TRUE, SINO RETORNA FALSE
def existePersona(documento,que_persona):
   
    estudiante = Estudiante.objects.filter(documento=documento)
    profesor = Profesor.objects.filter(documento=documento)
    #SI ES ESTUDIANTE, VERIFICA SI EXISTE EN EL MODEL ESTUDIANTE
    if que_persona == "Est":
        if estudiante.exists():
            return True
        else:
            return False
    #SI NO ES ESTUDIANTE, VERIFICARA SI EXISTE EN EL MODEL PROFESOR
    else:
        if profesor.exists():
            return True
        else:
            return False
#VERIFICA EXISTENCIA DE LA COMISION DEL NUEVO CURSO A INGRESAR
def existeCurso(comision):
    curso = Curso.objects.filter(comision=comision)

    if curso.exists():
        return True
    else:
        return False

#FUNCIONES QUE RENDERIZAN LOS DIFERENTES FORMULARIOS
def inicio(req):
    return render(req,"inicio.html",{'active_page': 'inicio'})

#RENDERIZA FORMULARIO DE INGRESO DE ESTUDIANTE, ADEMAS DE REALIZAR EL INGRESO DEL MISMO
def estudianteForm(req):
 
    try:
       
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
    # MANEJA ERRORES OPERATIVOS CON LA BASE DE DATOS
        return render(req, "Estudiantes/estudiantes.html", {'error_message':f"Ha ocurrido un error no controlado con la base de datos: {str(e)}",'active_page': 'estudiantes'})
    except IntegrityError as e:
    # MANEJA ERRORES DE INTEGRIDAD CON LA BASE DE DATOS
        return render(req, "Estudiantes/estudiantes.html", {'error_message':f"Ha ocurrido un error de integridad no controlado con la base de datos: {str(e)}",'active_page': 'estudiantes'})
    except ValueError as e:
    # MANEJA ERRORES DE VALOR
        return render(req, "Estudiantes/estudiantes.html", {'error_message':f"Se deben ingresar los datos: {str(e)}",'active_page': 'estudiantes'})
    except Exception as e:
    # CUALQUIERA OTRA EXCEPCIÓN NO CONTROLADA
        return render(req, "Estudiantes/estudiantes.html", {'error_message':f"Excepción no controlada: {str(e)}",'active_page': 'estudiantes'})

#RENDERIZA EL FORMULARIO DE CONSULTAS DE UN CIERTO ESTUDIANTE
def buscarEstudianteX(req):
    try:
        if req.GET["documentoEstudiante"]:

            documento = req.GET["documentoEstudiante"]

            estudiante = Estudiante.objects.filter(documento=documento)

            return render(req, "Estudiantes/formConsultarEstudiante.html", {"estudiantes": estudiante, "documento": documento,'active_page': 'estudiantes'})

        else:
            
            return render(req, "Estudiantes/formConsultarEstudiante.html", {"error_message": "No envias el dato del estudiante",'active_page': 'estudiantes'})
    except OperationalError as e:
    # MANEJA ERRORES OPERATIVOS CON LA BASE DE DATOS
        return render(req, "Estudiantes/formConsultarEstudiante.html", {'error_message':f"Ha ocurrido un error no controlado con la base de datos: {str(e)}",'active_page': 'estudiantes'})
    except IntegrityError as e:
    # MANEJA ERRORES DE INTEGRIDAD CON LA BASE DE DATOS
        return render(req, "Estudiantes/formConsultarEstudiante.html", {'error_message':f"Ha ocurrido un error de integridad no controlado con la base de datos: {str(e)}",'active_page': 'estudiantes'})
    except ValueError as e:
    # MANEJA ERRORES DE VALOR
        return render(req, "Estudiantes/formConsultarEstudiante.html", {'error_message':f"Se deben ingresar los datos: {str(e)}",'active_page': 'estudiantes'})
    except Exception as e:
    # CUALQUIERA OTRA EXCEPCIÓN NO CONTROLADA
        return render(req, "Estudiantes/formConsultarEstudiante.html", {'error_message':f"Excepción no controlada: {str(e)}",'active_page': 'estudiantes'})

#RENDERIZA EL FORMULARIO DE CONSULTAS DE TODOS LOS ESTUDIANTES
def buscarEstudiantesTodos(req):
    try:
        if req.method == "GET":
            estudiantes = Estudiante.objects.all()
            return render(req, "Estudiantes/formConsultarTodosEstudiantes.html", {"estudiantes": estudiantes,'active_page': 'estudiantes'})
    except OperationalError as e:
    # MANEJA ERRORES OPERATIVOS CON LA BASE DE DATOS
        return render(req, "Estudiantes/formConsultarTodosEstudiantes.html", {'error_message':f"Ha ocurrido un error no controlado con la base de datos: {str(e)}",'active_page': 'estudiantes'})
    except IntegrityError as e:
    # MANEJA ERRORES DE INTEGRIDAD CON LA BASE DE DATOS
        return render(req, "Estudiantes/formConsultarTodosEstudiantes.html", {'error_message':f"Ha ocurrido un error de integridad no controlado con la base de datos: {str(e)}",'active_page': 'estudiantes'})
    except ValueError as e:
    # MANEJA ERRORES DE VALOR
        return render(req, "Estudiantes/formConsultarTodosEstudiantes.html", {'error_message':f"Se deben ingresar los datos: {str(e)}",'active_page': 'estudiantes'})
    except Exception as e:
    # CUALQUIERA OTRA EXCEPCIÓN NO CONTROLADA
        return render(req, "Estudiantes/formConsultarTodosEstudiantes.html", {'error_message':f"Excepción no controlada: {str(e)}",'active_page': 'estudiantes'})

#RENDERIZA FORMULARIO DE INGRESO DE CURSO, ADEMAS DE REALIZAR EL INGRESO DEL MISMO
def cursoForm(req):
        try:
            
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
    # MANEJA ERRORES OPERATIVOS CON LA BASE DE DATOS
            return render(req, "Cursos/cursos.html", {'error_message':f"Ha ocurrido un error no controlado con la base de datos: {str(e)}",'active_page': 'cursos'})
        except IntegrityError as e:
    # MANEJA ERRORES DE INTEGRIDAD CON LA BASE DE DATOS
            return render(req, "Cursos/cursos.html", {'error_message':f"Ha ocurrido un error de integridad no controlado con la base de datos: {str(e)}",'active_page': 'cursos'})
        except ValueError as e:
    # MANEJA ERRORES DE VALOR
            return render(req, "Cursos/cursos.html", {'error_message':f"Se deben ingresar los datos: {str(e)}",'active_page': 'cursos'})
        except Exception as e:
    # CUALQUIERA OTRA EXCEPCIÓN NO CONTROLADA
            return render(req, "Cursos/cursos.html", {'error_message':f"Excepción no controlada: {str(e)}",'active_page': 'cursos'})

#RENDERIZA EL FORMULARIO DE CONSULTAS DE UN CIERTO CURSO SEGUN COMISION
def buscarCursoY(req):
    try:
        if req.GET["comisionCurso"]:

            comision = req.GET["comisionCurso"]

            curso = Curso.objects.filter(comision=comision)

            return render(req, "Cursos/formConsultarCurso.html", {"cursos": curso, "comision": comision,'active_page': 'cursos'})

        else:
      
            return render(req, "Cursos/formConsultarCurso.html", {"error_message": "No envias el dato del curso",'active_page': 'cursos'})  
    except OperationalError as e:
    # MANEJA ERRORES OPERATIVOS CON LA BASE DE DATOS
        return render(req, "Cursos/formConsultarCurso.html", {'error_message':f"Ha ocurrido un error no controlado con la base de datos: {str(e)}",'active_page': 'cursos'})
    except IntegrityError as e:
    # MANEJA ERRORES DE INTEGRIDAD CON LA BASE DE DATOS
        return render(req, "Cursos/formConsultarCurso.html", {'error_message':f"Ha ocurrido un error de integridad no controlado con la base de datos: {str(e)}",'active_page': 'cursos'})
    except ValueError as e:
    # MANEJA ERRORES DE VALOR
        return render(req, "Cursos/formConsultarCurso.html", {'error_message':f"Se deben ingresar los datos: {str(e)}",'active_page': 'cursos'})
    except Exception as e:
    # CUALQUIERA OTRA EXCEPCIÓN NO CONTROLADA
        return render(req, "Cursos/formConsultarCurso.html", {'error_message':f"Excepción no controlada: {str(e)}",'active_page': 'cursos'})

#RENDERIZA EL FORMULARIO DE CONSULTAS DE TODOS LOS CURSOS
def buscarCursosTodos(req):
    try:
        if req.method == "GET":
            estudiantes = Curso.objects.all()
            return render(req, "Cursos/formConsultarTodosCursos.html", {"cursos": estudiantes,'active_page': 'cursos'})
    
    except OperationalError as e:
    # MANEJA ERRORES OPERATIVOS CON LA BASE DE DATOS
        return render(req, "Cursos/formConsultarTodosCursos.html", {'error_message':f"Ha ocurrido un error no controlado con la base de datos: {str(e)}",'active_page': 'cursos'})
    except IntegrityError as e:
    # MANEJA ERRORES DE INTEGRIDAD CON LA BASE DE DATOS
        return render(req, "Cursos/formConsultarTodosCursos.html", {'error_message':f"Ha ocurrido un error de integridad no controlado con la base de datos: {str(e)}",'active_page': 'cursos'})
    except ValueError as e:
    # MANEJA ERRORES DE VALOR
        return render(req, "Cursos/formConsultarTodosCursos.html", {'error_message':f"Se deben ingresar los datos: {str(e)}",'active_page': 'cursos'})
    except Exception as e:
    # CUALQUIERA OTRA EXCEPCIÓN NO CONTROLADA
        return render(req, "Cursos/formConsultarTodosCursos.html", {'error_message':f"Excepción no controlada: {str(e)}",'active_page': 'cursos'})

#RENDERIZA FORMULARIO DE INGRESO DE PROFESOR, ADEMAS DE REALIZAR EL INGRESO DEL MISMO
def profesorForm(req):
    try:    
        
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
    # MANEJA ERRORES OPERATIVOS CON LA BASE DE DATOS
        return render(req, "Profesores/profesores.html", {'error_message':f"Ha ocurrido un error no controlado con la base de datos: {str(e)}",'active_page': 'profesores'})
    except IntegrityError as e:
    # MANEJA ERRORES DE INTEGRIDAD CON LA BASE DE DATOS
        return render(req, "Profesores/profesores.html", {'error_message':f"Ha ocurrido un error de integridad no controlado con la base de datos: {str(e)}",'active_page': 'profesores'})
    except ValueError as e:
    # MANEJA ERRORES DE VALOR
        return render(req, "Profesores/profesores.html", {'error_message':f"Se deben ingresar los datos: {str(e)}",'active_page': 'profesores'})
    except Exception as e:
    # CUALQUIERA OTRA EXCEPCIÓN NO CONTROLADA
        return render(req, "Profesores/profesores.html", {'error_message':f"Excepción no controlada: {str(e)}",'active_page': 'profesores'})

#RENDERIZA EL FORMULARIO DE CONSULTAS DE UN CIERTO PROFESOR SEGUN DOCUMENTO
def buscarProfesorZ(req):
    try:
        if req.GET["documentoProfesor"]:

            documento = req.GET["documentoProfesor"]

            profesor = Profesor.objects.filter(documento=documento)

            return render(req, "Profesores/formConsultarProfesor.html", {"profesores": profesor, "documento": documento,'active_page': 'profesores'})

        else:
      
            return render(req, "Profesores/formConsultarProfesor.html", {"error_message": "No envias el dato del curso",'active_page': 'profesores'})
    except OperationalError as e:
    # MANEJA ERRORES OPERATIVOS CON LA BASE DE DATOS
        return render(req, "Profesores/formConsultarProfesor.html", {'error_message':f"Ha ocurrido un error no controlado con la base de datos: {str(e)}",'active_page': 'profesores'})
    except IntegrityError as e:
    # MANEJA ERRORES DE INTEGRIDAD CON LA BASE DE DATOS
        return render(req, "Profesores/formConsultarProfesor.html", {'error_message':f"Ha ocurrido un error de integridad no controlado con la base de datos: {str(e)}",'active_page': 'profesores'})
    except ValueError as e:
    # MANEJA ERRORES DE VALOR
        return render(req, "Profesores/formConsultarProfesor.html", {'error_message':f"Se deben ingresar los datos: {str(e)}",'active_page': 'profesores'})
    except Exception as e:
    # CUALQUIERA OTRA EXCEPCIÓN NO CONTROLADA
        return render(req, "Profesores/formConsultarProfesor.html", {'error_message':f"Excepción no controlada: {str(e)}",'active_page': 'profesores'})
    
#RENDERIZA EL FORMULARIO DE CONSULTAS DE TODOS LOS PROFESORES
def buscarProfesoresTodos(req):
    try:
        if req.method == "GET":
            profesores = Profesor.objects.all()
            return render(req, "Profesores/formConsultarTodosProfesores.html", {"profesores": profesores,'active_page': 'profesores'})
    except OperationalError as e:
    # MANEJA ERRORES OPERATIVOS CON LA BASE DE DATOS
        return render(req, "Profesores/formConsultarTodosProfesores.html", {'error_message':f"Ha ocurrido un error no controlado con la base de datos: {str(e)}",'active_page': 'profesores'})
    except IntegrityError as e:
    # MANEJA ERRORES DE INTEGRIDAD CON LA BASE DE DATOS
        return render(req, "Profesores/formConsultarTodosProfesores.html", {'error_message':f"Ha ocurrido un error de integridad no controlado con la base de datos: {str(e)}",'active_page': 'profesores'})
    except ValueError as e:
    # MANEJA ERRORES DE VALOR
        return render(req, "Profesores/formConsultarTodosProfesores.html", {'error_message':f"Se deben ingresar los datos: {str(e)}",'active_page': 'profesores'})
    except Exception as e:
    # CUALQUIERA OTRA EXCEPCIÓN NO CONTROLADA
        return render(req, "Profesores/formConsultarTodosProfesores.html", {'error_message':f"Excepción no controlada: {str(e)}",'active_page': 'profesores'})

#RENDERIZA FORMULARIO DE INGRESO DE ENTREGABLES, ADEMAS DE REALIZAR EL INGRESO DEL MISMO
def entregablesForm(req):
    try:
       
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
    # MANEJA ERRORES OPERATIVOS CON LA BASE DE DATOS
        return render(req, "Entregables/entregables.html", {'error_message':f"Ha ocurrido un error no controlado con la base de datos: {str(e)}",'active_page': 'entregables'})
    except IntegrityError as e:
    # MANEJA ERRORES DE INTEGRIDAD CON LA BASE DE DATOS
        return render(req, "Entregables/entregables.html", {'error_message':f"Ha ocurrido un error de integridad no controlado con la base de datos: {str(e)}",'active_page': 'entregables'})
    except ValueError as e:
    # MANEJA ERRORES DE VALOR
        return render(req, "Entregables/entregables.html", {'error_message':f"Se deben ingresar los datos: {str(e)}",'active_page': 'entregables'})
    except Exception as e:
    # CUALQUIERA OTRA EXCEPCIÓN NO CONTROLADA
        return render(req, "Entregables/entregables.html", {'error_message':f"Excepción no controlada: {str(e)}",'active_page': 'entregables'})

#RENDERIZA EL FORMULARIO DE CONSULTAS DE LOS ENTREGABLES SEGUN LA FECHA INGRESADA
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
    # MANEJA ERRORES OPERATIVOS CON LA BASE DE DATOS
        return render(req, "Entregables/formConsultarEntregable.html", {'error_message':f"Ha ocurrido un error no controlado con la base de datos: {str(e)}",'active_page': 'entregables'})
    except IntegrityError as e:
    # MANEJA ERRORES DE INTEGRIDAD CON LA BASE DE DATOS
        return render(req, "Entregables/formConsultarEntregable.html", {'error_message':f"Ha ocurrido un error de integridad no controlado con la base de datos: {str(e)}",'active_page': 'entregables'})
    except ValueError as e:
    # MANEJA ERRORES DE VALOR
        return render(req, "Entregables/formConsultarEntregable.html", {'error_message':f"Se deben ingresar los datos: {str(e)}",'active_page': 'entregables'})
    except Exception as e:
    # CUALQUIERA OTRA EXCEPCIÓN NO CONTROLADA
        return render(req, "Entregables/formConsultarEntregable.html", {'error_message':f"Excepción no controlada: {str(e)}",'active_page': 'entregables'})

#RENDERIZA EL FORMULARIO DE CONSULTAS DE TODOS LOS ENTREGABLES
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
    # MANEJA ERRORES OPERATIVOS CON LA BASE DE DATOS
        return render(req, "Entregables/formConsultarTodosEntregables.html", {'error_message':f"Ha ocurrido un error no controlado con la base de datos: {str(e)}",'active_page': 'entregables'})
    except IntegrityError as e:
    # MANEJA ERRORES DE INTEGRIDAD CON LA BASE DE DATOS
        return render(req, "Entregables/formConsultarTodosEntregables.html", {'error_message':f"Ha ocurrido un error de integridad no controlado con la base de datos: {str(e)}",'active_page': 'entregables'})
    except ValueError as e:
    # MANEJA ERRORES DE VALOR
        return render(req, "Entregables/formConsultarTodosEntregables.html", {'error_message':f"Se deben ingresar los datos: {str(e)}",'active_page': 'entregables'})
    except Exception as e:
    # CUALQUIERA OTRA EXCEPCIÓN NO CONTROLADA
        return render(req, "Entregables/formConsultarTodosEntregables.html", {'error_message':f"Excepción no controlada: {str(e)}",'active_page': 'entregables'})