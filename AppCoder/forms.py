from django import forms

class EstudianteFormulario(forms.Form):
    documento = forms.CharField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.CharField()
    telefono = forms.CharField()