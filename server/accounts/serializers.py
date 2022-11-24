from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie, Crew, Genre

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('username',)


class UserProfileSerializer(serializers.ModelSerializer):

    class movieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('id', 'title', 'release_date', 'img_url', 'backdrop_img_url',)

    watchlist_movies = movieSerializer(many=True, read_only=True)
    like_movies = movieSerializer(many=True, read_only=True)
    followings = serializers.IntegerField(source='followings.count', read_only=True)
    followers = serializers.IntegerField(source='followers.count', read_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'profile_img', 'introduce', 'followings', 'followers', 'like_movies', 'watchlist_movies',)


class UserProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('username', 'introduce', 'profile_img',)


class followSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('username', 'profile_img', 'introduce', 'followers',)


class watchlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id',)