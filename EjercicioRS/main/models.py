from django.db import models

class Movie(models.Model):
    idPelicula = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=255)
    Director = models.CharField(max_length=255)
    idIMDB = models.CharField(max_length=20)
    Generos = models.CharField(max_length=255)

    def __str__(self):
        return self.Titulo

class Rating(models.Model):
    IdUsuario = models.IntegerField()
    idPelicula = models.ForeignKey(Movie, on_delete=models.CASCADE)
    Puntuacion = models.FloatField()

    def __str__(self):
        return f'User {self.IdUsuario} rated {self.idPelicula.Titulo} with {self.Puntuacion}'