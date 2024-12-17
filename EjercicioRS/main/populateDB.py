import pandas as pd
from .models import Pelicula, Puntuacion

def populate():
    # Cargar datos del dataset
    peliculas_df = pd.read_csv('path/to/peliculas.csv')
    puntuaciones_df = pd.read_csv('path/to/puntuaciones.csv')
    
    # Poblar la base de datos
    for _, row in peliculas_df.iterrows():
        Pelicula.objects.create(
            idPelicula=row['idPelicula'],
            titulo=row['titulo'],
            director=row['director'],
            idIMDB=row['idIMDB'],
            generos=row['generos']
        )
    
    for _, row in puntuaciones_df.iterrows():
        Puntuacion.objects.create(
            idUsuario=row['idUsuario'],
            idPelicula=Pelicula.objects.get(idPelicula=row['idPelicula']),
            puntuacion=row['puntuacion']
        )
