# import sys, os
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

from .models import Movie, Crew, Genre
import requests
from django.shortcuts import get_object_or_404, get_list_or_404
API_KEY = 'c355457ba4508bf477d4c1d98ce31dd0'

def makeDB():
    POPULAR_MOVIE_URL = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ko-KR&page='
    # GENRE_URL = f'https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=ko-KR'
            
    # 장르 데이터 추가
    # genre_data = requests.get(GENRE_URL).json()['genres']
    # for data in genre_data:
    #     genre = Genre.objects.create(pk=data['id'], name=data['name'])
        

    for num in range(1, 501):
        url = POPULAR_MOVIE_URL + str(num)
        movie_data = requests.get(url).json().get('results')

        for movie in movie_data:
            movie_id = movie.get('id')
            # title = movie.get('title')
            # description = movie.get('overview')
            # release_date =  movie.get('release_date')
            # img_url = movie.get('poster_path')
            # genre_ids = movie.get('genre_ids')
            # vote_average = movie.get('vote_average')
            popularity = movie.get('popularity')

            if movie_id and popularity:
                if Movie.objects.filter(pk=movie_id).exists():
                    m = Movie.objects.get(pk=movie_id)
                    
                    m.popularity = popularity
                    m.save()

def makeCrewDB():
    movies = Movie.objects.all()
    crew_ids = set()
    for movie in movies:                  
        Crew_URL = f'https://api.themoviedb.org/3/movie/{movie.pk}/credits?api_key={API_KEY}&language=ko-KR'
        cast_data = requests.get(Crew_URL).json().get('cast')
        for data in cast_data:
            if data['profile_path']:
                if data['id'] not in crew_ids:
                    crew_ids.add(data['id'])
                    at = Crew.objects.create(id=data['id'],name=data['name'], gender=data['gender'],job=data['known_for_department'], profile_img_path="https://image.tmdb.org/t/p/w500"+data['profile_path'],popularity=data['popularity'])
                else:
                    at = Crew.objects.get(pk=data['id'])
                # print(at.name)
                movie.crews.add(at)
        
        crew_data = requests.get(Crew_URL).json().get('crew')
        for data in crew_data:
            if data['profile_path'] and data['known_for_department'] =='Directing':
                if data['id'] not in crew_ids:
                    crew_ids.add(data['id'])
                    at = Crew.objects.create(id=data['id'],name=data['name'], gender=data['gender'],job=data['known_for_department'], profile_img_path="https://image.tmdb.org/t/p/w500"+data['profile_path'],popularity=data['popularity'])
                else:
                    at = Crew.objects.get(pk=data['id'])
                # print(at.name)
                movie.crews.add(at)
        


def makeMovieBackdrop():
    movies = get_list_or_404(Movie)
    MOVIE_DETAIL_URL = f'https://api.themoviedb.org/3/movie/'
    # 영화아이디?api_key=에이피아이&language=ko-KR'
    for movie in movies:
        movieId = movie.id
        url = f'{MOVIE_DETAIL_URL}{movieId}?api_key={API_KEY}&language=ko-KR'
        result = requests.get(url).json().get('backdrop_path')
        backdrop_url = f'https://image.tmdb.org/t/p/original{result}'
        target = Movie.objects.get(pk=movieId)
        target.backdrop_img_url = backdrop_url
        target.save()