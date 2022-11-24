from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model

from .serializers import UserSerializer, UserProfileSerializer, followSerializer, UserProfileUpdateSerializer, watchlistSerializer

from movies.models import Movie
# Create your views here.

# 회원가입
@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    password = request.data.get('password')
    password_confirm = request.data.get('password_confirm')

    # 비밀번호 검증
    if password != password_confirm:
        context = {'password_unmatch': '비밀번호가 일치하지 않습니다.',}
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    elif not password:
        context = {'password': '비밀번호를 입력해주세요.',}
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(password)
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE'])
def profile(request, username):
    profile_user = get_object_or_404(get_user_model(), username=username)
    # 프로필 조회
    if request.method == 'GET':
        serializer = UserProfileSerializer(profile_user)
        if profile_user.followers.filter(pk=request.user.pk).exists():
            is_follow = 'Unfollow' 
        else:
            is_follow = 'Follow' 
        context = {
            'is_follow': is_follow,
        }
        context.update(serializer.data)
        return Response(context)
    
    # 계정 삭제
    elif request.data.get('username') == request.user.username:
        if request.method == 'DELETE':
            profile_user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        context = {
            'faild': '실패'
        }
    return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def update(request, username):
    if request.user.username == username:
        user = get_object_or_404(get_user_model(), username=username)
        # 프로필 수정 페이지 조회
        if request.method == 'GET':
            serializer = UserProfileUpdateSerializer(user)
            return Response(serializer.data)
        
        # 프로필 수정
        elif request.method == 'PUT':
            password = request.data.get('password')
            password_confirm = request.data.get('password_confirm')
            profile_img = request.FILES.get('profile_img')
            introduce = request.data.get('introduce')

            # 비밀번호 검증
            if password and password != password_confirm:
                context = {'password_unmatch': '비밀번호가 일치하지 않습니다.',}
                return Response(context, status=status.HTTP_400_BAD_REQUEST)

            # 프로필 수정
            else:
                if password != 'null':
                    user.set_password(password)
                print(user.password)
                user.introduce = introduce if introduce else user.introduce
                user.profile_img = profile_img if profile_img else user.profile_img
                user.save()
                context = {'success': '수정이 완료되었습니다.'}
                return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        message = '자신의 프로필만 수정할 수 있습니다.'
    context ={'message': message}
    return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def follow(request, username, page_name):
    user = get_user_model()
    me = request.user
    you = get_object_or_404(user, username=username)

    # 팔로우
    if request.method == 'POST':
        if me != you:
            if you.followers.filter(username=me.username).exists():
                # 언팔로우
                you.followers.remove(me)
                message = 'Follow'
            else:
                # 팔로우
                you.followers.add(me)
                message = 'Unfollow'
            context = {'message': message,}
            return Response(context, status=status.HTTP_200_OK)
        context = {'message': '자기 자신을 팔로우할 수 없습니다.',}
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    # followItems
    else:
        # 팔로워
        if page_name == 'followers':
            follows = you.followers.all()
            serializer = followSerializer(follows, many=True)
            for user in serializer.data:
                if me.pk in user.get('followers'):
                    user['is_follow'] = 'Unfollow'
                else:
                    user['is_follow'] = 'Follow'
            return Response(serializer.data)
        # 팔로잉
        elif page_name == 'followings':
            follows = you.followings.all()
            serializer = followSerializer(follows, many=True)
            for user in serializer.data:
                if me.pk in user.get('followers'):
                    user['is_follow'] = 'Unfollow'
                else:
                    user['is_follow'] = 'Follow'
            return Response(serializer.data)


@api_view(['GET', 'POST'])
def watchlist(requset, movie_pk):
    user = requset.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    if requset.method == 'POST':
        if user.watchlist_movies.filter(pk=movie_pk).exists():
            user.watchlist_movies.remove(movie)
            message = False
        else:
            user.watchlist_movies.add(movie)
            message = True
        context = {'message': message,}
        return Response(context, status=status.HTTP_201_CREATED)
    else:
        watchlists = user.watchlist_movies.all()
        serializer = watchlistSerializer(watchlists, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def like_movies(requset, movie_pk):
    user = requset.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    if requset.method == 'POST':
        if user.like_movies.filter(pk=movie_pk).exists():
            user.like_movies.remove(movie)
            message = False
        else:
            user.like_movies.add(movie)
            message = True
        context = {'message': message,}
        return Response(context, status=status.HTTP_201_CREATED)
    else:
        likes = user.like_movies.all()
        serializer = watchlistSerializer(likes, many=True)
        return Response(serializer.data)