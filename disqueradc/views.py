from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def inicio(request):
#     return HttpResponse('<h1>Bienvenido a la app</h1>')

def index(request):
    return render(request,'artistas/index.html')

def disquera(request):
    return render(request,'disqueras.html')

def genero(request):
    return render(request,'generos.html')

def addartista(request):
    return render(request,'artistas/crear.html')

def editartista(request):
    return render(request,'artistas/editar.html')