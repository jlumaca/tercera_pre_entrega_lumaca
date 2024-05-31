from django import forms

class EstudianteFormulario(forms.Form):
    documento = forms.CharField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.CharField()
    telefono = forms.CharField()

class CursoFormulario(forms.Form):
    nombre = forms.CharField()
    comision = forms.IntegerField()


class ProfesorFormulario(forms.Form):
    documento = forms.CharField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.CharField()
    telefono = forms.CharField()
    curso = forms.CharField()

class EntregableFormulario(forms.Form):
    nombre = forms.CharField()
    fecha_de_entrega = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class': 'form-control', 'placeholder': 'Fecha de Entrega'}))
    entregado = forms.BooleanField()