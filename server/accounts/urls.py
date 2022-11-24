from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup),
    path('likemovie/<int:movie_pk>/', views.like_movies),
    path('watchlist/<int:movie_pk>/', views.watchlist),
    path('<str:username>/', views.profile),
    path('<str:username>/update/', views.update),
    path('<str:username>/<str:page_name>/', views.follow),
]
