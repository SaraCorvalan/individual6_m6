from django.shortcuts import render
from django.contrib.auth import authenticate, login
from aplicacion_5.models import registroClientes
from .forms import registroForm, LoginForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# CLIENTES


def primeraFuncion(request):
    return render(request, 'landing.html')

@login_required
def formularioContacto(request):
    data = {
        'form': registroForm()
    }
    if request.method == 'POST':
        formulario = registroForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "CLIENTE REGISTRADO !!!"
        else:
            data["form"] = formulario
    return render(request, 'registro_clientes.html', data)

@login_required
def informeUsuarios(request):
     #'usuarios' es una instancia de la clase "registroUsuarios" definida en models.py
    usuarios = registroClientes.objects.all()
    return render(request, 'salida_clientes.html', {'usuarios': usuarios})
##############################################################################################


# USUARIOS
def user_login(request):
    
    if request.method == 'POST':
        formulario = LoginForm(data=request.POST)
        if formulario.is_valid():
           usuario = formulario.cleaned_data['usuario']
           password = formulario.cleaned_data['password']
           user = authenticate(request, username=usuario, password=password)
           if user is not None:
               if user.is_active:
                   login(request, user)
                   #messages.success(request, f"Autentificación exitosa, estimado(a) {usuario}")
                   return render(request, 'registration/bienvenida.html', {'users': usuario})
                   #return HttpResponse(f"Autentificación exitosa, estimado(a) {usuario}")
               else:
                   messages.error(request, "Cuenta no habilitada")
                   #return HttpResponse("Cuenta NO habilitada")
           else:
               #return HttpResponse("Login No válido")
                messages.error(request, "Login no válido")
    else:
        formulario = LoginForm()

    return render(request, 'registration/login.html', {'formulario': formulario})


              

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }   
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
           formulario.save()
           usuario = formulario.cleaned_data['username']
           password = formulario.cleaned_data['password1']
           user = authenticate(request, username=usuario, password=password)       
           login(request, user)
           return render(request, 'registration/bienvenida.html', {'users': usuario})
           messages.success(request, f"Te has registrado correctamente, estimado(a) {usuario}")           
        data['form'] = formulario

    return render(request, 'registration/registro.html', data)
