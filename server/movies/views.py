# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.decorators import api_view


# from rest_framework import status
# from .models import Movie, Crew
# from .serializers import MovieListSerializer, CrewListSerializer, GenreListSerializer, MovieSerializer, CrewSerializer

# # Create your views here.
# @api_view(['GET'])
# def movies_list(request, movies_filter):
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
    
# @api_view(['GET'])
# def movies_detail(request, movie_pk):
#     movie = Movie.objects.get(pk=movie_pk)
#     serializer = MovieSerializer(movie)
#     return Response(serializer.data)

# @api_view(['GET'])
# def crews_list(request):
#     crews = Crew.objects.all()
#     serializer = CrewListSerializer(crews)
#     return Response(serializer.data)

# @api_view(['GET'])
# def crews_detail(request, crew_pk):
#     crew = Crew.objects.get(pk=crew_pk)
#     serializer = CrewSerializer(crew)
#     return Response(serializer.data)

# @api_view(['GET'])
# def director_list(request):
#     crews = Crew.objects.all()

#     serializer = CrewListSerializer(crews)
#     return Response(serializer.data)
    




