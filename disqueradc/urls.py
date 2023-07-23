from django.urls import *
from . import views

urlpatterns = [
    path('base', views.inicio, name='inicio'),

    path('views/disqueras', views.disquera, name='disquera'),
    path('disqueras/add', views.adddisquera, name='disquera-add'),
    path('disquera/edit', views.editdisquera, name='disquera-edit'),

    path('views/generos', views.genero, name='genero'),
    path('generos/add', views.addgenero, name='genero-add'),
    path('generos/edit', views.editgenero, name='genero-edit'),

    path('views/artistas', views.artista, name='artista'),
    path('artista/add', views.addartista, name='artista-add'),
    path('artista/edit', views.editartista, name='artista-edit'),

    path('views/albumes', views.album, name='album'),
    path('albumes/add', views.addalbum, name='album-add'),
    path('albumes/edit', views.editalbum, name='album-edit'),

    path('views/canciones', views.cancion, name='cancion'),
    path('canciones/add', views.addcancion, name='cancion-add'),
    path('canciones/edit', views.editcancion, name='cancion-edit'),

]