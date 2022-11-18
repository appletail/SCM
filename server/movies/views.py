# from django.shortcuts import render
# from rest_framework.response import Response
# from .models import Movie, Crew

# # Create your views here.
# def movies(request, movies_filter):
#     movies = Movie.objects.all()

#     if movies_filter == 'popular':
#         movies = sorted(movies, key=lambda x: x.vote_average)
        
#         return
#     elif movies_filter == 'personal':
        
#         return
#     elif movies_filter == 'latest':
#         movies = sorted(movies, key=lambda x:x.release_date)
#         return
        
#     elif movies_filter == 'upcoming':
#         return
    
