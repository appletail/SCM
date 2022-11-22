from rest_framework import serializers
from .models import Movie, Crew, Genre

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'img_url',)


class CrewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Crew
        fields = ('id', 'name','profile_img_path', 'job',)


class GenreListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name')


class GenreSerializer(serializers.ModelSerializer):
    
    movies = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = '__all__'


class CrewSerializer(serializers.ModelSerializer):

    movies = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = Crew
        fields = '__all__'
        # read_only_fields = ('id', 'movies',)


class MovieSerializer(serializers.ModelSerializer):

    crews = CrewListSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
