import pandas as pd
from django.shortcuts import get_object_or_404, render, redirect

from EjercicioRS import settings
from main.forms import AnimeRecomendacionForm, UsuarioBusquedaForm
from main.recommendations import calculateSimilarItems, getRecommendations, transformPrefs
from .models import Anime, Rating
from django.db.models import Count, Avg

def index(request):
    return render(request, 'index.html',{'STATIC_URL':settings.STATIC_URL})


def loadDict():
    Prefs = {}  
    
    ratings = Rating.objects.select_related('anime').all()
    
    for rating in ratings:
        user = int(rating.user_id)
        anime_id = int(rating.anime.anime_id)
        score = float(rating.rating)
        
        Prefs.setdefault(user, {})  
        Prefs[user][anime_id] = score 

    ItemsPrefs = transformPrefs(Prefs)
    SimItems = calculateSimilarItems(Prefs, n=10)

    return {"Prefs": Prefs, "ItemsPrefs": ItemsPrefs, "SimItems":SimItems}

def cargar_base_datos(request):
    if request.method == 'POST':
        Anime.objects.all().delete()
        Rating.objects.all().delete()

        anime_data = pd.read_csv('data/anime.csv', sep=';') 
        puntuacion_data = pd.read_csv('data/ratings.csv', sep=';') 

        animes = [
            Anime(
                anime_id=row['anime_id'],
                name=row['name'],
                genre=row['genre'],
                type=row['type'],
                episodes=row['episodes']
            )
            for _, row in anime_data.iterrows()
        ]
        Anime.objects.bulk_create(animes)

        puntuaciones = [
            Rating(
                user_id=row['user_id'],
                anime=Anime.objects.get(anime_id=row['anime_id']),
                rating=row['rating']
            )
            for _, row in puntuacion_data.iterrows()
        ]
        Rating.objects.bulk_create(puntuaciones)

        return render(request, 'carga_exitosa.html', {"mensaje": "Datos cargados correctamente",
                                                      'animes': animes,
                                                      "puntuaciones":puntuaciones})
    
    return render(request, 'confirmar_carga.html')


def animes_por_genero(request):
    generos = set()
    for anime in Anime.objects.values_list('genre', flat=True):
        if anime:
            generos.update([g.strip() for g in anime.split(',')])

    animes_filtrados = None
    genero_seleccionado = None

    if request.method == "POST":
        genero_seleccionado = request.POST.get('genero')

        animes_filtrados = Anime.objects.filter(
            genre__icontains=genero_seleccionado
        ).values(
            'type'
        ).annotate(
            total=Count('anime_id')
        ).order_by('type')

    return render(request, 'animes_por_genero.html', {
        'generos': sorted(generos),  
        'animes_filtrados': animes_filtrados, 
        'genero_seleccionado': genero_seleccionado})
    
    
def mejores_animes(request):
    animes_con_puntuacion = (
        Rating.objects.values('anime_id', 'name')
        .annotate(puntuacion_media=Avg('rating'))
        .order_by('-puntuacion_media')[:3]
    )

    mejores_animes = []
    animes_dict = {anime.anime_id: anime for anime in Anime.objects.all()}  

    for anime in animes_con_puntuacion:
        anime_id = anime['anime_id']
        anime_titulo = anime['name']
        anime_puntuacion = round(anime['puntuacion_media'], 2)
        
        anime_actual = animes_dict.get(anime_id)
        
        mejores_animes.append({
            'titulo': anime_titulo,
            'puntuacion_media': anime_puntuacion,
        })

    return render(request, 'mejores_animes.html', {'mejores_animes': mejores_animes})


def construir_prefs():
    prefs = {}
    ratings = Rating.objects.select_related('anime').all()
    
    for rating in ratings:
        user_id = rating.user_id
        anime_id = rating.anime.anime_id
        score = rating.rating
        
        prefs.setdefault(user_id, {})
        prefs[user_id][anime_id] = score
    
    return prefs

    
    
def mejores_animes(request):
    animes_top = (
        Rating.objects.values('anime__name')
        .annotate(puntuacion_media=Avg('rating')) 
        .order_by('-puntuacion_media')[:3] 
    )


    return render(request, 'mejores_animes.html', {'animes_top':animes_top})

def recomendar_animes_usuario(request):
    formulario = UsuarioBusquedaForm()
    items = None
    usuario = None

    if request.method == 'POST':
        formulario = UsuarioBusquedaForm(request.POST)
        
        if formulario.is_valid():
            id_usuario = int(formulario.cleaned_data['idUsuario'])
            formato_seleccionado = formulario.cleaned_data['formato']

            
            # usuario = get_object_or_404(Rating, user_id=id_usuario)

            prefs = {}
            ratings = Rating.objects.select_related('anime').all()
            for r in ratings:
                prefs.setdefault(r.user_id, {})
                prefs[r.user_id][r.anime.anime_id] = r.rating

            recomendaciones = getRecommendations(prefs, int(id_usuario))

            animes_puntuados = set(
                r.anime.anime_id for r in Rating.objects.filter(user_id=id_usuario)
            )
            animes_recomendados = [
                (Anime.objects.get(anime_id=anime_id), puntuacion)
                for puntuacion, anime_id in recomendaciones
                if Anime.objects.get(anime_id=anime_id).type == formato_seleccionado
                and anime_id not in animes_puntuados
            ][:2]

            items = zip([anime for anime, _ in animes_recomendados], 
                        [puntuacion for _, puntuacion in animes_recomendados])
    
    return render(request, 'recomendar_animes_usuario.html', {
        'formulario': formulario,
        'items': items,
        # 'usuario': usuario,
        'STATIC_URL': settings.STATIC_URL})