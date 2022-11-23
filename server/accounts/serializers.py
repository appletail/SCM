from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('username',)


class UserProfileSerializer(serializers.ModelSerializer):

    followings = serializers.IntegerField(source='followings.count', read_only=True)
    followers = serializers.IntegerField(source='followers.count', read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('username', 'profile_img', 'introduce', 'followings', 'followers',)


class UserProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('username', 'introduce', 'profile_img',)


class followSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('username', 'profile_img', 'introduce', 'followers',)