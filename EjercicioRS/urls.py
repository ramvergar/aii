from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cargar_base_datos/', views.cargar_base_datos, name='cargar_base_datos'),
    path('cargar_recsys/', views.cargar_recsys, name='cargar_recsys'),
    path('peliculas_por_genero/', views.peliculas_por_genero, name='peliculas_por_genero'),
    path('peliculas_mas_puntuadas/', views.peliculas_mas_puntuadas, name='peliculas_mas_puntuadas')
]
