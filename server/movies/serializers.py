from rest_framework import serializers
from .models import Movie, Crew, Genre
from reviews.serializers import ReviewListSerializer
from django.contrib.auth import get_user_model

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'img_url', 'release_date', 'description', 'popularity',)


class CrewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Crew
        fields = ('id', 'name','profile_img_path', 'job',)


class GenreListSerializer(serializers.ModelSerializer):

    movies = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = '__all__'


class CrewSerializer(serializers.ModelSerializer):
    movies = MovieListSerializer(many=True, read_only=True)
    genres = GenreListSerializer(many=True, read_only=True)

    class Meta:
        model = Crew
        fields = '__all__'
        # read_only_fields = ('id', 'movies',)


class MovieSerializer(serializers.ModelSerializer):
    review_set = ReviewListSerializer(many=True, read_only=True)
    crews = CrewListSerializer(many=True, read_only=True)
    genres = GenreListSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


class recommendSerializer(serializers.ModelSerializer):

    class movieSerializer(serializers.ModelSerializer):

        class genreSerializer(serializers.ModelSerializer):

            class Meta:
                model = Genre
                fields = ('id', 'name',)

        genres = genreSerializer(many=True, read_only=True)

        class Meta:
            model = Movie
            fields = ('genres',)

    watchlist_movies = movieSerializer(many=True, read_only=True)
    like_movies = movieSerializer(many=True, read_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ('like_movies', 'watchlist_movies',)