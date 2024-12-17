from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.db import models
from django import forms
from django.contrib.auth.decorators import login_required
import csv

# Models
class Pelicula(models.Model):
    idPelicula = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=200)
    Director = models.CharField(max_length=200)
    idIMDB = models.CharField(max_length=50)
    Generos = models.CharField(max_length=200)

class Puntuacion(models.Model):
    idUsuario = models.IntegerField()
    idPelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    Puntuacion = models.IntegerField(choices=[(i, str(i)) for i in range(10, 55, 5)])

# Forms
class ConfirmForm(forms.Form):
    confirm = forms.BooleanField(required=True)

class PeliculaForm(forms.Form):
    genero = forms.CharField(max_length=200)

class RecomendacionForm(forms.Form):
    titulo = forms.CharField(max_length=200)

# Views
def cargar_base_datos(request):
    if request.method == 'POST':
        form = ConfirmForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            Pelicula.objects.all().delete()
            Puntuacion.objects.all().delete()
            with open('path/to/dataset.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    pelicula = Pelicula.objects.create(
                        Titulo=row['Titulo'],
                        Director=row['Director'],
                        idIMDB=row['idIMDB'],
                        Generos=row['Generos']
                    )
                    Puntuacion.objects.create(
                        idUsuario=row['idUsuario'],
                        idPelicula=pelicula,
                        Puntuacion=row['Puntuacion']
                    )
            return HttpResponse("Base de datos cargada correctamente.")
    else:
        form = ConfirmForm()
    return render(request, 'confirm.html', {'form': form})

def cargar_recsys(request):
    # Implementar la lógica para cargar los datos necesarios para el sistema de recomendación
    return HttpResponse("Sistema de recomendación cargado.")

def peliculas_por_generos(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            genero = form.cleaned_data['genero']
            peliculas = Pelicula.objects.filter(Generos__icontains=genero).order_by('Director')
            return render(request, 'movie_list.html', {'peliculas': peliculas})
    else:
        form = PeliculaForm()
    return render(request, 'genero_form.html', {'form': form})

def peliculas_mas_puntuadas(request):
    peliculas = Puntuacion.objects.values('idPelicula').annotate(count=models.Count('idPelicula')).order_by('-count')[:2]
    peliculas_info = []
    for pelicula in peliculas:
        pelicula_obj = Pelicula.objects.get(idPelicula=pelicula['idPelicula'])
        similares = get_similar_movies(pelicula_obj)
        peliculas_info.append({'pelicula': pelicula_obj, 'similares': similares})
    return render(request, 'top_movies.html', {'peliculas_info': peliculas_info})

def recomendar_usuarios(request):
    if request.method == 'POST':
        form = RecomendacionForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            pelicula = Pelicula.objects.get(Titulo=titulo)
            usuarios = get_recommended_users(pelicula)
            return render(request, 'user_recommendations.html', {'usuarios': usuarios})
    else:
        form = RecomendacionForm()
    return render(request, 'recomendacion_form.html', {'form': form})

# Helper functions
def get_similar_movies(pelicula):
    # Implementar la lógica para obtener películas similares
    return []

def get_recommended_users(pelicula):
    # Implementar la lógica para obtener usuarios recomendados
    return []

# URL Configuration
from django.urls import path

urlpatterns = [
    path('cargar_base_datos/', cargar_base_datos, name='cargar_base_datos'),
    path('cargar_recsys/', cargar_recsys, name='cargar_recsys'),
    path('peliculas_por_generos/', peliculas_por_generos, name='peliculas_por_generos'),
    path('peliculas_mas_puntuadas/', peliculas_mas_puntuadas, name='peliculas_mas_puntuadas'),
    path('recomendar_usuarios/', recomendar_usuarios, name='recomendar_usuarios'),
]