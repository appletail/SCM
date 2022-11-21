from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .makeDB import makeDB, makeCrewDB
from .models import Movie, Crew
from .serializers import MovieListSerializer, CrewListSerializer, GenreListSerializer, MovieSerializer, CrewSerializer
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model


# movies 조회
@api_view(['GET'])
def movies_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def movies_list_popular(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        movies = sorted(movies, key=lambda x: x.vote_average)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def movies_list_personal(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        # movies = sorted(movies, key=lambda x: x.vote_average)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def movies_list_latest(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        movies = sorted(movies, key=lambda x:x.release_date)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def movies_list_latest(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        # upcoming 받아오는,
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

# movie detail
@api_view(['GET'])
def movies_detail(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

@api_view(['GET'])
def crews_list(request):
    if request.method == 'GET':
        crews = get_list_or_404(Crew)
        serializer = CrewListSerializer(crews)
        return Response(serializer.data)

@api_view(['GET'])
def crews_detail(request, crew_pk):
    if request.method == 'GET':
        crew = get_object_or_404(Crew,pk=crew_pk)
        serializer = CrewSerializer(crew)
        return Response(serializer.data)

@api_view(['GET'])
def director_list(request):
    if request.method == 'GET':
        crews = get_list_or_404(Crew)

        serializer = CrewListSerializer(crews)
        return Response(serializer.data)
    
# @api_view(['GET'])  
# def makedb(request):
#     makeDB()
#     makeCrewDB()
#     return 



