from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Movie, Rating
from .recommendations import load_data, get_movie_recommendations, get_most_rated_movies

# View for loading the database from the dataset
def load_database(request):
    if request.method == 'POST':
        load_data()  # Function to load data from dataset
        return redirect('index')
    return render(request, 'recommendations/load_database.html')

# View for displaying movies by genre
@login_required
def movies_by_genre(request, genre):
    movies = Movie.objects.filter(genres__icontains=genre)
    return render(request, 'recommendations/movie_list.html', {'movies': movies})

# View for showing the most rated movies
@login_required
def most_rated_movies(request):
    movies = get_most_rated_movies()
    return render(request, 'recommendations/movie_list.html', {'movies': movies})

# View for recommending movies based on a movie
@login_required
def recommend_movies(request, movie_id):
    recommendations = get_movie_recommendations(movie_id)
    return render(request, 'recommendations/recommendations.html', {'recommendations': recommendations})