from rest_framework import serializers
from .models import Review, ReviewComment


class ReviewListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'title', 'content','user', 'username')
        read_only_fields = ('user',)


class ReviewCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReviewComment
        fields = '__all__'
        read_only_fields = ('review','user',)


class ReviewSerializer(serializers.ModelSerializer):
    comment_set = ReviewCommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'like_users','comment_set')



