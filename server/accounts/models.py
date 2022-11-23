import os
import shutil

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from movies.models import Movie

# Create your models here.
def user_img_path(instance, filename):
    return f'images/{instance.username}/profile/{filename}'

class User(AbstractUser):
    introduce = models.CharField(max_length=100)
    profile_img = models.ImageField(blank=True, upload_to=user_img_path)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    watchlist_movies = models.ManyToManyField(Movie, related_name='watchlist_users')
    like_movies = models.ManyToManyField(Movie, related_name='like_users')
    
    def delete(self, *args, **kwargs):
        dir_path = f'{settings.MEDIA_ROOT}/images/{self.username}'
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)
        super(User, self).delete(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        img_path = f'{settings.MEDIA_ROOT}/images/{self.username}/profile'
        if self.profile_img and os.path.exists(img_path):
            img_list = os.listdir(img_path)
            for img in img_list:
                os.remove(os.path.join(img_path, img))
        super().save(*args, **kwargs)