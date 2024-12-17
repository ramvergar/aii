from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('index.html/', views.index),
    path('confirmar_carga/',views.cargar_base_datos),
    path('', views.index),
    path('animes_por_genero/', views.animes_por_genero, name='animes_por_genero'),
    path('mejores_animes/', views.mejores_animes, name='mejores_animes'),
    path('mejores_animes/', views.mejores_animes, name='mejores_animes'),
    path('recomendar_animes_usuario/', views.recomendar_animes_usuario, name='recomendar_animes_usuario'),
    ]
