from django.db import models
from django.conf import settings
from movies.models import Movie

# Create your models here.
class Review(models.Model):
    # movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    title = models.CharField(max_length=30)
    content = models.TextField()
    Lookup_cnt = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ReviewComment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)