from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('movies/', views.movie_list, name='movie_list'),
    path('recommendations/', views.recommendations_view, name='recommendations'),
]