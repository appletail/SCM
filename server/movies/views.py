from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .makeDB import makeDB, makeCrewDB
from .models import Movie, Crew, Genre
from .serializers import MovieListSerializer, CrewListSerializer, GenreListSerializer, GenreSerializer, MovieSerializer, CrewSerializer
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model

# 인기영화 조회
@api_view(['GET'])
def movies_list_popular(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        movies = sorted(movies, key=lambda x: x.popularity, reverse=True)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


# 최신영화 조회
@api_view(['GET'])
def movies_list_latest(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        movies = sorted(movies, key=lambda x:x.release_date, reverse=True)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


# 장르리스트 조회
@api_view(['GET'])
def movies_list_genre(request):
    if request.method == 'GET':
        genre = get_list_or_404(Genre)
        serializer = GenreListSerializer(genre, many=True)
        return Response(serializer.data)


# 장르별 영화 조회
@api_view(['GET'])
def genre_detail(request, genre_pk):
    if request.method == 'GET':
        movies = Movie.objects.all().filter(genres=genre_pk).order_by('-popularity')
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


# 맞춤영화 짜야함
@api_view(['GET'])
def movies_list_personal(request):
    pass


# 영화 상세 조회
@api_view(['GET'])
def movies_detail(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


# 배우리스트 조회
@api_view(['GET'])
def crews_list(request, page):
    if request.method == 'GET':
        pages = page * 50
        crews = Crew.objects.all().filter(job='Acting').order_by('id')[pages - 50 : pages]
        # crews = crews.filter(job='Acting')
        serializer = CrewListSerializer(crews, many=True)
        return Response(serializer.data)


# 감독리스트 조회
@api_view(['GET'])
def director_list(request, page):
    if request.method == 'GET':
        pages = page * 50
        crews = Crew.objects.all().filter(job='Directing').order_by('id')[pages - 50 : pages]
        serializer = CrewListSerializer(crews, many=True)
        return Response(serializer.data)


# 영화 관련자 상세 조회
@api_view(['GET'])
def crews_detail(request, crew_pk):
    if request.method == 'GET':
        crew = get_object_or_404(Crew,pk=crew_pk)
        serializer = CrewSerializer(crew)
        return Response(serializer.data)


# @api_view(['GET'])  
# def makedb(request):
#     makeDB()
#     makeCrewDB()
#     return Response()
