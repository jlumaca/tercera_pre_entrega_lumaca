from django import forms

#FORMULARIOS DE INGRESO DE DATOS CON LOS ESTILOS INCLUIDOS
class EstudianteFormulario(forms.Form):
    documento = forms.CharField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',  # Clase CSS
            'placeholder': 'Documento',  # Placeholder como en el form HTML
        })
    )
    nombre = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',  # Clase CSS
            'placeholder': 'Nombre',  # Placeholder para nombre
        })
    )
    apellido = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',  # Clase CSS
            'placeholder': 'Apellido',  # Placeholder para apellido
        })
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',  # Clase CSS
            'placeholder': 'Email',  # Placeholder para email
        })
    )
    telefono = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',  # Clase CSS
            'placeholder': 'Teléfono',  # Placeholder para teléfono
        })
    )

    submit = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'type': 'submit',
            'class': 'btn btn-block btn-bold btn-primary',
            'value': 'Guardar'
        })
    )

    buscar = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'type': 'submit',
            'class': 'btn btn-block btn-bold btn-primary',
            'value': 'Buscar'
        })
    )

class CursoFormulario(forms.Form):
    nombre = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',  # Clase CSS
            'placeholder': 'Nombre del curso',  # Placeholder para teléfono
        })

    )
    comision = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',  # Clase CSS
            'placeholder': 'Número de comisión',  # Placeholder para teléfono
        })
    )

    submit = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'type': 'submit',
            'class': 'btn btn-block btn-bold btn-primary',
            'value': 'Guardar'
        })
    )

    buscar = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'type': 'submit',
            'class': 'btn btn-block btn-bold btn-primary',
            'value': 'Buscar'
        })
    )


class ProfesorFormulario(forms.Form):
    documento = forms.CharField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',  # Clase CSS
            'placeholder': 'Documento',  # Placeholder para teléfono
        })

    )
    nombre = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',  # Clase CSS
            'placeholder': 'Nombre',  # Placeholder para teléfono
        })

    )
    apellido = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',  # Clase CSS
            'placeholder': 'Apellido',  # Placeholder para teléfono
        })
    )
    email = forms.CharField(
        required=False,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',  # Clase CSS
            'placeholder': 'Correo electrónico',  # Placeholder para teléfono
        })
    )
    telefono = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',  # Clase CSS
            'placeholder': 'Teléfono',  # Placeholder para teléfono
        }))
    curso = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',  # Clase CSS
            'placeholder': 'Curso',  # Placeholder para teléfono
        })
    )

    submit = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'type': 'submit',
            'class': 'btn btn-block btn-bold btn-primary',
            'value': 'Guardar'
        })
    )

    buscar = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'type': 'submit',
            'class': 'btn btn-block btn-bold btn-primary',
            'value': 'Buscar'
        })
    )

class EntregableFormulario(forms.Form):
    nombre = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',  # Clase CSS
            'placeholder': 'Nombre',  # Placeholder para teléfono
        })
    )
    fecha_de_entrega = forms.DateField(required=False,widget=forms.DateInput(attrs={'type':'date','class': 'form-control', 'placeholder': 'Fecha de Entrega'}))
    entregado = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
        })
    )

    submit = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'type': 'submit',
            'class': 'btn btn-block btn-bold btn-primary',
            'value': 'Guardar'
        })
    )

    buscar = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'type': 'submit',
            'class': 'btn btn-block btn-bold btn-primary',
            'value': 'Buscar'
        })
    )