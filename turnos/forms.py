from django import forms

class CrearUsuario(forms.Form):
    usuario = forms.CharField(label='Usuario', max_length=30, widget = forms.TextInput(attrs={'class' : 'input'}))
    clave = forms.CharField(label='Contrasenia', max_length=30, widget = forms.TextInput(attrs={'class' : 'input'}))
    nombre = forms.CharField(label='Nombre', max_length=30, widget = forms.TextInput(attrs={'class' : 'input'}))
    apellido = forms.CharField(label='Apellido', max_length=30, widget = forms.TextInput(attrs={'class' : 'input'}))
    correo = forms.EmailField()
    telefono = forms.IntegerField()

class CrearTurno(forms.Form):
#    usuario = forms.CharField(label='Usuario', max_length=30, widget = forms.TextInput(attrs={'class' : 'input'}))
    fecha = forms.DateField(label='Fecha' ,widget=forms.DateInput(format='%Y-%m-%d'))#forms.DateInput())
    hora = forms.TimeField(label='Hora',widget=forms.TimeInput(format='%H:%M'))
#    disponible = forms.BooleanField(label='Disponible',widget=forms.BooleanField())


   # fecha = forms.DateField()#forms.DateInput())
   # hora = forms.TimeField()
