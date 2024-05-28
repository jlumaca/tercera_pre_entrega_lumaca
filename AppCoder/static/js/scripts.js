/*!
* Start Bootstrap - Landing Page v6.0.6 (https://startbootstrap.com/theme/landing-page)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-landing-page/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

function opcionFormEstudiantes() {
    var selectedOption = document.getElementById("opcionEst").value;
    var documentoField = document.getElementById("documentoEst");
    var nombreField = document.getElementById("nombreEst");
    var apellidoField = document.getElementById("apellidoEst");
    var emailField = document.getElementById("emailEst");
    var telefonoField = document.getElementById("telefonoEst");
    var btnEnviar = document.getElementById("btnEnviarEst");
    var btnBuscar = document.getElementById("btnBuscarEst");
    var btnBuscarTodos = document.getElementById("btnTodosEst");
    var tituloForm = document.getElementById("tituloFormEst");

    if (selectedOption == "ingresoEst") {
        tituloForm.textContent = "Ingresar nuevo estudiante";
        documentoField.style.display = "block";
        nombreField.style.display = "block";
        apellidoField.style.display = "block";
        emailField.style.display = "block";
        telefonoField.style.display = "block";
        btnEnviar.style.display = "block";
        btnBuscar.style.display = "none";
        btnBuscarTodos.style.display = "none";
    } else if (selectedOption == "consultarEst"){
        tituloForm.textContent = "Consultar estudiante";
        documentoField.style.display = "block";
        nombreField.style.display = "none";
        apellidoField.style.display = "none";
        emailField.style.display = "none";
        telefonoField.style.display = "none";
        btnBuscar.style.display = "block";
        btnEnviar.style.display = "none";
        btnBuscarTodos.style.display = "none";
    } else {
        tituloForm.textContent = "Consultar estudiantes";
        documentoField.style.display = "none";
        nombreField.style.display = "none";
        apellidoField.style.display = "none";
        emailField.style.display = "none";
        telefonoField.style.display = "none";
        btnBuscar.style.display = "none";
        btnEnviar.style.display = "none";
        btnBuscarTodos.style.display = "block";

    }
}

function prueba(){
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

function prueba2(){
    var selectedOption = document.getElementById("opcionEst");

    var url = selectedOption.options[selectedOption.selectedIndex].value;
    if (url) {  // Verifica que la opción seleccionada tenga una URL
        window.location.href = url;
    }
}