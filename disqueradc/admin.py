from django.contrib import admin
from .models import *
# Register your models here.

# .site Registar todos los modelos de la aplicacion
# .registe método 

admin.site.register(Disquera)
admin.site.register(Artista)
admin.site.register(Album)
admin.site.register(Genero)
admin.site.register(Cancion)
