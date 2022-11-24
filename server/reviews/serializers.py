from rest_framework import serializers
from .models import Review, ReviewComment
from movies.models import Movie
from django.contrib.auth import get_user_model

class movieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title',)


class ReviewListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    like_users_count = serializers.IntegerField(source='like_users.count', read_only=True)
    movie = movieSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'movie','title', 'content','user', 'username', 'like_users_count','created_at','Lookup_cnt')
        read_only_fields = ('user',)


class ReviewCommentSerializer(serializers.ModelSerializer):

    class userSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('username', 'profile_img',)
    user = userSerializer(read_only=True)
    class Meta:
        model = ReviewComment
        fields = '__all__'
        read_only_fields = ('review',)


class ReviewSerializer(serializers.ModelSerializer):

    reviewcomment_set = ReviewCommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='reviewcomment_set.count', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    movie = movieSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'like_users',)

class ReviewCreateSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Review
        fields = ('title','content')
        read_only_fields = ('user', 'movie',)



