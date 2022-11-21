from rest_framework import serializers
from .models import Movie, Crew, Genre

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'img_url','movie_id',)

class CrewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Crew
        fields = ('name','profile_img_path')

class GenreListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'
        read_only_fields = ('movies',)

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

class CrewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Crew
        fileds = '__all__'
        read_only_fields = ('movies',)
