from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def inicio(request):
#     return HttpResponse('<h1>Bienvenido a la app</h1>')

def inicio(request):
    return render(request, 'base.html')

def save(request):
    return render()

def disquera(request):
    return render(request, 'disqueras/index.html')
def adddisquera(request):
    return render(request, 'disqueras/crear.html')
def editdisquera(request):
    return render(request, 'disqueras/editar.html')

def genero(request):
    return render(request, 'generos/index.html')
def addgenero(request):
    return render(request, 'generos/crear.html')
def editgenero(request):
    return render(request, 'generos/editar.html')

def artista(request):
    return render(request, 'artistas/index.html')
def addartista(request):
    return render(request, 'artistas/crear.html')
def editartista(request):
    return render(request, 'artistas/editar.html')

def album(request):
    return render(request, 'albumes/index.html')
def addalbum(request):
    return render(request, 'albumes/crear.html')
def editalbum(request):
    return render(request, 'albumes/editar.html')

def cancion(request):
    return render(request, 'canciones/index.html')
def addcancion(request):
    return render(request, 'canciones/crear.html')
def editcancion(request):
    return render(request, 'canciones/editar.html')