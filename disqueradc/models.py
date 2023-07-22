from django.db import models

# Create your models here.

class Disquera(models.Model):
    id=models.AutoField(primary_key=True)
    nitDisquera=models.CharField(max_length=25)
    nombreDisquera=models.CharField(max_length=100)
    telefonoDisquera=models.CharField(max_length=15)
    direccionDisquera=models.CharField(max_length=100)
    estadoDisquera=models.BooleanField()

class Artista(models.Model):
    id=models.AutoField(primary_key=True)
    noDocumento=models.CharField(max_length=20)
    tipoDocumento=models.CharField(max_length=20)
    nombreArtista=models.CharField(max_length=50)
    apellidoArtista=models.CharField(max_length=50)
    nombreArtistico=models.CharField(max_length=50)
    fNacimArtista=models.DateField(null=True, blank=True)
    emailArtista=models.CharField(max_length=100)
    fotoArtista=models.ImageField(upload_to='imagenes/', null=True, blank=True)
    idDisqueraFK=models.ForeignKey(Disquera,on_delete=models.CASCADE)
    estadoArtista=models.BooleanField()

class Genero(models.Model):
    id=models.AutoField(primary_key=True)
    nombreGenero=models.CharField(max_length=50)
    estadoGenero=models.BooleanField()

class Album(models.Model):
    id=models.AutoField(primary_key=True)
    nombreAlbum=models.CharField(max_length=100)
    anioPublicacion=models.CharField(max_length=5)
    idArtistaFK=models.ForeignKey(Artista,on_delete=models.CASCADE)
    idGeneroFk=models.ForeignKey(Genero,on_delete=models.CASCADE)
    fotoAlbum=models.ImageField(upload_to='imagenes/', null=True, blank=True)
    estadoAlbum=models.BooleanField()

class Cancion(models.Model):
    id=models.AutoField(primary_key=True)
    nombreCancion=models.CharField(max_length=100)
    duracionCancion=models.IntegerField()
    idAlbumFK=models.ForeignKey(Album,on_delete=models.CASCADE)
    estadoCancion=models.BooleanField()