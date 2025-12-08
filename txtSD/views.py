from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate 
from .forms import RegistroForm, UsuarioCreationForm, UsuarioChangeForm
from .models import Usuario  
from django.contrib.auth.hashers import make_password


def registro_usuario(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UsuarioCreationForm()

    return render(request, 'registro.html', {'form': form})

def editar_usuario(request):
    if request.method == 'POST':
        form = UsuarioChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = UsuarioChangeForm(instance=request.user)

    return render(request, 'editar.html', {'form': form})


def perfil(request):
    usuario = request.user
    return render(request, 'perfilUsuario.html', {'usuario': usuario})

def index(request):
    return render(request, 'index.html')

def quiz(request):
    return render(request, 'quiz.html')

def login_view(request):
    return render(request, 'login.html')

def perfil(request):
    return render(request, 'perfilUsuario.html')

def ingresoUsuarios(request):
    return render(request, 'ingresoUsuarios.html')

def antesEmpezar(request):
    return render(request, 'antesEmpezar.html')

def listaQuiz(request):
    return render(request, 'listaQuiz.html')

def quizBasica1(request):
    return render(request, 'quizBasica1.html')

def quizBasica2(request):
    return render(request, 'quizBasica2.html')

def quizBasica3(request):
    return render(request, 'quizBasica3.html')

def quizBasica4(request):
    return render(request, 'quizBasica4.html')

def retroalimentacion(request):
    return render(request, 'retroalimentacion.html')

def retroalimentacionA(request):
    return render(request, 'retroalimentacionA.html')

def retroalimentacionG(request):
    return render(request, 'retroalimentacionG.html')

def retroalimentacionC(request):
    return render(request, 'retroalimentacionC.html')

def historiaBasica(request):
    return render(request, 'historiaBasica.html')

def oro1(request):
    return render(request, 'oro1.html')

def plata1(request):
    return render(request, 'plata1.html')

def bronce1(request):
    return render(request, 'bronce1.html')

def sinMedalla1(request):
    return render(request, 'sinMedalla1.html')

def historiaMedia(request):
    return render(request, 'historiaMedia.html')

def antesEmpezarMedia(request):
    return render(request, 'antesEmpezarMedia.html')

def quizMedia1(request):
    return render(request, 'quizMedia1.html')

def juego(request):
    return render(request, 'juego.html')


