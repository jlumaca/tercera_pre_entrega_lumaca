function opcionesEst(){
    var selectedOption = document.getElementById("opcionEst").value;
    var formIngEst = document.getElementById("FormIngresarEstudiante");
    var formConsEst = document.getElementById("FormConsultarEstudiante");
    var formConsEstTodos = document.getElementById("FormConsultarEstudiantesTodos");

    if (selectedOption == "ingresoEst"){
        formIngEst.style.display = "block";
        formConsEst.style.display = "none";
        formConsEstTodos.style.display = "none";
    }else if (selectedOption == "consultarEst"){
        formIngEst.style.display = "none";
        formConsEst.style.display = "block";
        formConsEstTodos.style.display = "none";
    }else {
        formIngEst.style.display = "none";
        formConsEst.style.display = "none";
        formConsEstTodos.style.display = "block";
    }
}


function opcionesCursos(){
    var selectedOption = document.getElementById("opcionCursos").value;
    var formIngCurso = document.getElementById("FormIngresarCurso");
    var formConsCurso = document.getElementById("FormConsultarCurso");
    var formConsCursosTodos = document.getElementById("FormConsultarCursosTodos");

    if (selectedOption == "ingresoCurso"){
        formIngCurso.style.display = "block";
        formConsCurso.style.display = "none";
        formConsCursosTodos.style.display = "none";
    }else if (selectedOption == "consultarCurso"){
        formIngCurso.style.display = "none";
        formConsCurso.style.display = "block";
        formConsCursosTodos.style.display = "none";
    }else {
        formIngCurso.style.display = "none";
        formConsCurso.style.display = "none";
        formConsCursosTodos.style.display = "block";
    }
}



function opcionesProf(){
    var selectedOption = document.getElementById("opcionProf").value;
    var formIngProfesor = document.getElementById("FormIngresarProfesor");
    var formConsProfesor = document.getElementById("FormConsultarProfesor");
    var formConsProfesoresTodos = document.getElementById("FormConsultarProfesoresTodos");

    if (selectedOption == "ingresoProf"){
        formIngProfesor.style.display = "block";
        formConsProfesor.style.display = "none";
        formConsProfesoresTodos.style.display = "none";
    }else if (selectedOption == "consultarProf"){
        formIngProfesor.style.display = "none";
        formConsProfesor.style.display = "block";
        formConsProfesoresTodos.style.display = "none";
    }else {
        formIngProfesor.style.display = "none";
        formConsProfesor.style.display = "none";
        formConsProfesoresTodos.style.display = "block";
    }
}

function opcionesEntregables(){
    var selectedOption = document.getElementById("opcionEntregables").value;
    var formIngEntregable = document.getElementById("FormIngresarEntregable");
    var formConsEntregable = document.getElementById("FormConsultarEntregable");
    var formConsEntregablesTodos = document.getElementById("FormConsultarEntregablesTodos");

    if (selectedOption == "ingresoEntregables"){
        formIngEntregable.style.display = "block";
        formConsEntregable.style.display = "none";
        formConsEntregablesTodos.style.display = "none";
    }else if (selectedOption == "consultarEntregables"){
        formIngEntregable.style.display = "none";
        formConsEntregable.style.display = "block";
        formConsEntregablesTodos.style.display = "none";
    }else {
        formIngEntregable.style.display = "none";
        formConsEntregable.style.display = "none";
        formConsEntregablesTodos.style.display = "block";
    }
}


