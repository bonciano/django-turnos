from django.contrib.auth.models import User
from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .forms import CrearTurno, CrearMensaje
from .models import Turnos, Mensajes
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
import calendar
import datetime



# Create your views here.
# Sitio base

def index(request):
    return render(request, 'index.html')

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


# Menu de usuarios

@login_required
def listarturno(request,usuario_id):
    if request.method == 'GET':
        usuario_id = 3
        turno = Turnos.objects.filter(usuario_id = usuario_id)
        print(f'Aqui van los turnos del usuario 3: {turno}')
        return render(request, 'index.html', {
            'turno' : turno
            })



@login_required
def altaturno(request):
    if request.method == 'GET':
        c = calendar.Calendar()
        cal1 = []
        cal2 = []
        j = 0

        for i in c.itermonthdays(datetime.date.today().year,datetime.date.today().month):
            cal1.append(str(i))
            j+=1
            if j in (7,14,21,28):
                cal1.append('99')
                cal1.append('88')
        for i in c.itermonthdays(datetime.date.today().year,datetime.date.today().month+1):
            cal2.append(str(i))
            j+=1
            if j in (7,14,21,28):
                cal2.append('99')
                cal2.append('88')

        return render(request, 'turnos/altaturno.html',{'formturno' : CrearTurno(), 'cal1' : cal1, 'cal2' : cal2 })
    else:
        a = 'lucas'
        Turnos.objects.create(
            usuario_id = 3,
            fecha = request.POST['fecha'],
            hora = request.POST['hora'],
            disponible = True
        )
    return render(request,'index.html')


@login_required
def bajaturno(request):
    pass


@login_required
def eliminarturno(request):
    pass





# Registro de usuarios

def signup(request):

    if request.method == 'GET':
        return render(request, 'usuarios/signup.html',{
            'fsignup' : UserCreationForm
            })
    else:
        u = request.POST['username']
        p1 = request.POST['password1']
        p2 = request.POST['password2']
        if p1 == p2:
            try:
                usuario = User.objects.create_user(username=u,password=p1)
                usuario.save()
                login(request,usuario)
                return redirect('altaturno')
            except:
                return render(request, 'usuarios/signup.html', {
                    'fsignup' : UserCreationForm,
                    'error' : 'El usuario ya existe, por favor, ingresar otro nombre de usuario'
                    })
        else:
            return render(request, 'usuarios/signup.html', {
                'fsignup' : UserCreationForm,
                'error' : 'Las contrasenias no coinciden, por favor, vuelva a intentar'
                })


def signin(request):
    if request.method == 'GET':
        return render(request,'usuarios/signin.html', {'fsignin':AuthenticationForm})
    else:
        u = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if u is None:
            return render(request,'usuarios/signin.html',{'fsignin' : AuthenticationForm, 'error' : 'Usuario y/o contrasenia ivalidos'})
        else:
            login(request,u)
            return redirect('index')

@login_required
def signout(request):
    logout(request)
    return redirect('index')



