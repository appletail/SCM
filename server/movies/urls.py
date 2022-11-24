from django.urls import path
from . import views

urlpatterns = [
    path('savemovies/', views.save_movies),
    path('popular/<int:page>/',views.movies_list_popular),
    path('latest/<int:page>/',views.movies_list_latest),
    path('personal/<int:page>/',views.movies_list_personal),
    path('genre/',views.movies_list_genre),
    path('genre/<int:genre_pk>/',views.genre_detail),
    path('<int:movie_pk>/',views.movies_detail),
    path('crews/actor/<int:page>/',views.crews_list),
    path('crews/director/<int:page>/',views.director_list),
    path('crews/<int:crew_pk>/',views.crews_detail),
    path('makeDB/',views.makedb),
]
