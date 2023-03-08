from django.shortcuts import render, redirect
from .forms import CrearUsuario, CrearTurno, CrearMensaje
from .models import Usuarios, Turnos, Mensajes


# Create your views here.


def index(request):
    return render(request, 'index.html')



def altausuario(request):
    if request.method == 'GET':
        return render(request, 'usuarios/altausuario.html',{
            'formulario' : CrearUsuario()
            })
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



def listarturno(request,usuario_id):
    if request.method == 'GET':
        usuario_id = 3
        turno = Turnos.objects.filter(usuario_id = usuario_id)
        print(f'Aqui van los turnos del usuario 3: {turno}')
        return render(request, 'index.html', {
            'turno' : turno
            })



def altaturno(request):
    if request.method == 'GET':
        return render(request, 'turnos/altaturno.html',{
            'formturno' : CrearTurno()
            })
    else:
        a = 'lucas'
        Turnos.objects.create(
            usuario_id = 3,
            fecha = request.POST['fecha'],
            hora = request.POST['hora'],
            disponible = True
        )
    return render(request,'index.html')


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
    if request.method == 'GET':
        return render(request,'contacto.html',{
            'formulario' : CrearMensaje()
            })
    else:
        Mensajes.objects.create(
                usuario = 'lucas',
                nombre = request.POST['nombre'],
                correo = request.POST['correo'],
                telefono = request.POST['telefono'],
                mensaje = request.POST['mensaje']
                )
        return redirect('index')






