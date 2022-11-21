# import sys, os
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

from .models import Movie, Crew, Genre
import requests

API_KEY = 'c355457ba4508bf477d4c1d98ce31dd0'

def makeDB():
    POPULAR_MOVIE_URL = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ko-KR&page='
    GENRE_URL = f'https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=ko-KR'
            
    # 장르 데이터 추가
    genre_data = requests.get(GENRE_URL).json()['genres']
    for data in genre_data:
        genre = Genre.objects.create(pk=data['id'], name=data['name'])
        

    for num in range(1, 501):
        url = POPULAR_MOVIE_URL + str(num)
        movie_data = requests.get(url).json().get('results')

        for movie in movie_data:
            movie_id = movie.get('id')
            title = movie.get('title')
            description = movie.get('overview')
            release_date =  movie.get('release_date')
            img_url = movie.get('poster_path')
            genre_ids = movie.get('genre_ids')
            vote_average = movie.get('vote_average')

            if movie_id and title and description and release_date and img_url and genre_ids and vote_average:
                if not Movie.objects.filter(pk=movie_id).exists():
                    m = Movie.objects.create(pk=movie_id, title=title, description=description, release_date=release_date, img_url="https://image.tmdb.org/t/p/w500/" + img_url, vote_average=vote_average)

                    for genre in genre_ids:
                        g = Genre.objects.get(pk=genre)
                        m.genres.add(g)

def makeCrewDB():
    movies = Movie.objects.all()
    for movie in movies:                  
        Crew_URL = f'https://api.themoviedb.org/3/movie/{movie.pk}/credits?api_key={API_KEY}&language=ko-KR'
        cast_data = requests.get(Crew_URL).json().get('cast')
        for data in cast_data:
            if data['profile_path']:
                at = Crew.objects.create(name=data['name'], gender=data['gender'],job=data['known_for_department'], profile_img_path="https://image.tmdb.org/t/p/w500"+data['profile_path'],popularity=data['popularity'])
                # print(at.name)
                movie.crews.add(at)
        
        crew_data = requests.get(Crew_URL).json().get('crew')
        for data in crew_data:
            if data['profile_path'] and data['known_for_department'] =='Directing':
                at = Crew.objects.create(name=data['name'], gender=data['gender'],job=data['known_for_department'], profile_img_path="https://image.tmdb.org/t/p/w500"+data['profile_path'],popularity=data['popularity'])
                # print(at.name)
                movie.crews.add(at)

        


