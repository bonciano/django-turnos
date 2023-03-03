from django.shortcuts import render
from .forms import CrearUsuario
from .models import Usuarios


# Create your views here.


def index(request):
    return render(request, 'index.html')



def altausuario(request):
    if request.method == 'GET':
        return render(request, 'altausuario.html',{
            'formulario' : CrearUsuario()})
    else:
        Usuarios.objects.create(
            usuario = request.POST['usuario'],
            clave = request.POST['clave'],
            nombre = request.POST['nombre'],
            apellido = request.POST['apellido'],
            correo =  request.POST['correo'],
            telefono = request.POST['telefono']
        )
    return render(request,'index.html')

def listarturnos(request):
    pass



def altaturno(request):
    '''
    Para darme de alta en un turno, primero tengo que estar logueado.
    Y para estar logueado, primero debo estar registrado.
    Vinculo turno con usuario.
    El turno posee:
        fecha de alta del turno
        fecha del turno
        hora del turno
        usuario que solicito el turno
    '''
    pass


def bajaturno(request):
    pass


def iniciosesion(request):
    pass

def cerrarsesion(request):
    pass # ?????

def eliminarturno(request):
    pass


def sobre(request):
    return render(request,'sobre.html')



def contacto(request):
    return render(request,'contacto.html')








