import pandas as pd
from django.shortcuts import get_object_or_404, render, redirect
from django.db import connection

from EjercicioRS import settings
from main.forms import UsuarioBusquedaForm
from main.recommendations import calculateSimilarItems, getRecommendations, transformPrefs
from .models import Pelicula, Puntuacion
from django.db.models import Count, Avg

def index(request):
    return render(request, 'index.html', {'STATIC_URL': settings.STATIC_URL})

def loadDict():
    Prefs = {}  
    
    puntuaciones = Puntuacion.objects.select_related('idPelicula').all()
    
    for puntuacion in puntuaciones:
        user = int(puntuacion.idUsuario)
        pelicula_id = int(puntuacion.idPelicula.idPelicula)
        score = float(puntuacion.puntuacion)
        
        Prefs.setdefault(user, {})  
        Prefs[user][pelicula_id] = score

    return Prefs

def cargar_base_datos(request):
    if request.method == 'POST':
        # Borrar la base de datos
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM main_puntuacion")
            cursor.execute("DELETE FROM main_pelicula")
        
        # Cargar datos del dataset
        # Aquí se debe agregar el código para cargar los datos del dataset en la base de datos
        
        return redirect('index')
    return render(request, 'cargar_base_datos.html')

def cargar_recsys(request):
    loadDict()
    return redirect('index')

def peliculas_por_genero(request):
    generos = Pelicula.objects.values_list('generos', flat=True).distinct()
    peliculas = None
    if request.method == 'POST':
        genero = request.POST.get('genero')
        peliculas = Pelicula.objects.filter(generos__icontains=genero).order_by('director')
    return render(request, 'peliculas_por_genero.html', {'generos': generos, 'peliculas': peliculas})

def peliculas_mas_puntuadas(request):
    peliculas = Puntuacion.objects.values('idPelicula__titulo').annotate(num_puntuaciones=Count('puntuacion')).order_by('-num_puntuaciones')[:2]
    return render(request, 'peliculas_mas_puntuadas.html', {'peliculas': peliculas})
