from django.db import models

class Anime(models.Model):
    anime_id = models.IntegerField(primary_key=True)  
    name = models.CharField(max_length=255)  
    genre = models.CharField(max_length=500) 
    type = models.CharField(max_length=50) 
    episodes = models.CharField(max_length=255) 

    def _str_(self):
        return self.name


class Rating(models.Model):
    user_id = models.IntegerField()  
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, default=1)  
    rating = models.IntegerField()  

    def _str_(self):
        return f"Usuario {self.user_id} - {self.anime.name} - {self.rating}"