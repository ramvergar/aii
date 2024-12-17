from django.test import TestCase
from .models import Movie, Rating

class MovieModelTest(TestCase):
    def setUp(self):
        Movie.objects.create(Título="Inception", Director="Christopher Nolan", idIMDB="tt1375666", Géneros="Action, Sci-Fi")
        Movie.objects.create(Título="The Matrix", Director="Lana Wachowski, Lilly Wachowski", idIMDB="tt0133093", Géneros="Action, Sci-Fi")

    def test_movie_creation(self):
        inception = Movie.objects.get(Título="Inception")
        matrix = Movie.objects.get(Título="The Matrix")
        self.assertEqual(inception.Director, "Christopher Nolan")
        self.assertEqual(matrix.Géneros, "Action, Sci-Fi")

class RatingModelTest(TestCase):
    def setUp(self):
        movie = Movie.objects.create(Título="Inception", Director="Christopher Nolan", idIMDB="tt1375666", Géneros="Action, Sci-Fi")
        Rating.objects.create(IdUsuario=1, idPelicula=movie, Puntuación=5)

    def test_rating_creation(self):
        rating = Rating.objects.get(IdUsuario=1)
        self.assertEqual(rating.Puntuación, 5)