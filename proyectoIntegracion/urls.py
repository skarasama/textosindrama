"""
URL configuration for proyectoIntegracion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from txtSD import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('quiz/', views.quiz, name='quiz'),
    path('login/', views.login_view, name='login'),
    path('perfil/', views.perfil, name='perfil'),
    path('ingresoUsuarios/', views.ingresoUsuarios, name='ingresoUsuarios'),
    path('antesEmpezar/', views.antesEmpezar, name='antesEmpezar'),
    path('antesEmpezarMedia/', views.antesEmpezarMedia, name='antesEmpezarMedia'),
    path('listaQuiz/', views.listaQuiz, name='listaQuiz'),
    path('quizBasica1/', views.quizBasica1, name='quizBasica1'),
    path('quizMedia1/', views.quizMedia1, name='quizMedia1'),
    path('quizBasica2/', views.quizBasica2, name='quizBasica2'),
    path('quizBasica3/', views.quizBasica3, name='quizBasica3'),
    path('quizBasica4/', views.quizBasica4, name='quizBasica4'),
    path('historiaBasica/', views.historiaBasica, name='historiaBasica'),
    path('oro1/', views.oro1, name='oro1'),
    path('plata1/', views.plata1, name='plata1'),
    path('bronce1/', views.bronce1, name='bronce1'),
    path('sinMedalla1/', views.sinMedalla1, name='sinMedalla1'),
    path('historiaMedia/', views.historiaMedia, name='historiaMedia'),
    path('juego/', views.juego, name='juego'),
]
