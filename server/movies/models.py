from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    release_date = models.DateField(null=True)
    vote_average = models.FloatField(default=0, null=True)
    img_url = models.CharField(max_length=255, null=True)
    backdrop_img_url = models.CharField(max_length=255, null=True)


class Crew(models.Model):
    name = models.CharField(max_length=32)
    gender = models.IntegerField()
    job = models.CharField(max_length=255)
    movies = models.ManyToManyField(Movie, related_name='crews')
    popularity = models.FloatField()
    profile_img_path = models.CharField(max_length=255)


class Genre(models.Model):
    genre_id = models.IntegerField(default=-1)
    name = models.CharField(max_length=32)
    movies = models.ManyToManyField(Movie, related_name='genres')