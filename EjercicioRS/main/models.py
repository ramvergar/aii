from django.db import models

class Pelicula(models.Model):
    idPelicula = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    idIMDB = models.CharField(max_length=255)
    generos = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo

class Puntuacion(models.Model):
    idUsuario = models.IntegerField()
    idPelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()

    def __str__(self):
        return f'{self.idUsuario} - {self.idPelicula} - {self.puntuacion}'