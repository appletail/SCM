from rest_framework import serializers
from .models import Review, ReviewComment


class ReviewListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'title', 'content','author', 'username')


class ReviewCommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReviewComment
        fields = ('author', 'review')
        read_only_fields = ('review','author',)


class ReviewSerializer(serializers.ModelSerializer):
    comment_set = ReviewCommentListSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', )

class ReviewCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReviewComment
        fields = '__all__'
        read_only_fields = ('review','author',)


