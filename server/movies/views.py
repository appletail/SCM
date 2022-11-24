from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .makeDB import makeDB, makeCrewDB, makeMovieBackdrop
from .models import Movie, Crew, Genre
from .serializers import MovieListSerializer, CrewListSerializer, GenreListSerializer, MovieSerializer, CrewSerializer, recommendSerializer, GenreListSerializer
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model


# 영화 저장용
@api_view(['GET'])
def save_movies(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        movies = sorted(movies, key=lambda x: x.popularity, reverse=True)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


# 인기영화 조회
@api_view(['GET'])
def movies_list_popular(request, page):
    if request.method == 'GET':
        pages = 20 * page
        movies = Movie.objects.all().order_by('-popularity')[pages - 20 : pages]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


# 최신영화 조회
@api_view(['GET'])
def movies_list_latest(request, page):
    if request.method == 'GET':
        pages = 20 * page
        movies = get_list_or_404(Movie)
        movies = sorted(movies, key=lambda x:x.release_date, reverse=True)[pages - 20 : pages]
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
def movies_list_personal(request, page):
    user = request.user
    serializer = recommendSerializer(user)
    maxGenre = {}
    for like in serializer.data.get('like_movies'):
        for genre in like.get('genres'):
            name = genre.get('name')
            if maxGenre.get(name):
                maxGenre[name] += 1
            else:
                maxGenre[name] = 1

    for watch in serializer.data.get('watchlist_movies'):
        for genre in watch.get('genres'):
            name = genre.get('name')
            if maxGenre.get(name):
                maxGenre[name] += 1
            else:
                maxGenre[name] = 1
    maxGenre = sorted(maxGenre.items(), key= lambda x : x[1], reverse=True)
    if maxGenre:
        genre = get_object_or_404(Genre, name=maxGenre[0][0])
        serializer = GenreListSerializer(genre)
        pages = 20 * page
        data = sorted(serializer.data.get('movies'), key= lambda x : x.get('popularity'), reverse=True)[pages - 20 : pages]
        return Response(data)
    else:
        context = {'pick': '영화에 좋아요를 눌러주세요!'}
        return Response(context)
    

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


@api_view(['GET'])  
def makedb(request):
    user = request.user
    serializer = recommendSerializer(user)
    maxGenre = {}
    for like in serializer.data.get('like_movies'):
        for genre in like.get('genres'):
            name = genre.get('name')
            if maxGenre.get(name):
                maxGenre[name] += 1
            else:
                maxGenre[name] = 1

    for watch in serializer.data.get('watchlist_movies'):
        for genre in watch.get('genres'):
            name = genre.get('name')
            if maxGenre.get(name):
                maxGenre[name] += 1
            else:
                maxGenre[name] = 1
    maxGenre = sorted(maxGenre.items(), key= lambda x : x[1], reverse=True)
    print(maxGenre[0][0])
    return Response(serializer.data)
