from django.urls import *
from . import views

urlpatterns = [
    path('inicio/', views.index, name='inicio'),
    path('views/disqueras',views.disquera, name='disquera'),
    path('views/generos',views.genero, name='genero'),
    path('artista/add',views.addartista,name='artista-add'),
    path('artista/edit',views.editartista,name='artista-edit'),
]