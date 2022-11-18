from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie

# Create your models here.
class User(AbstractUser):
    introduce = models.CharField(max_length=100)
    nickname = models.CharField(max_length=15, null=True)
    # profile_img = models.ImageField()
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    watchlist_movies = models.ManyToManyField(Movie, related_name='watchlist_users')
    like_movies = models.ManyToManyField(Movie, related_name='like_users')
