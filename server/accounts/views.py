from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model

from .serializers import UserSerializer, UserProfileSerializer

# Create your views here.

# 회원가입
@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    password = request.data.get('password')
    password_confirm = request.data.get('password_confirm')
    nickname = request.data.get('nickname')

    # 비밀번호 검증
    if password != password_confirm:
        context = {'password_unmatch': '비밀번호가 일치하지 않습니다.',}
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(password)
        user.nickname = nickname if nickname else user.username
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE'])
def profile(request, username):
    profile_user = get_object_or_404(get_user_model(), username=username)
    serializer = UserProfileSerializer(profile_user)
    # 프로필 조회
    if request.method == 'GET':
        if profile_user.followers.filter(pk=request.user.pk).exists():
            is_follow = 'Unfollow' 
        else:
            is_follow = 'Follow' 
        context = {
            'username': profile_user.username,
            'nickname': profile_user.nickname,
            'introduce': profile_user.introduce,
            'following': profile_user.followings.all(),
            'follower': profile_user.followers.all(),
            'is_follow': is_follow,
        }

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
            context = {
                'username': user.username,
                'nickname': user.nickname,
                'introduce': user.introduce,
            }
            return Response(context)
        
        # 프로필 수정
        elif request.method == 'PUT':
            password = request.data.get('password')
            password_confirm = request.data.get('password_confirm')
            nickname = request.data.get('nickname')
            introduce = request.data.get('introduce')

            # 비밀번호 검증
            if password and password != password_confirm:
                context = {'password_unmatch': '비밀번호가 일치하지 않습니다.',}
                return Response(context, status=status.HTTP_400_BAD_REQUEST)

            # 프로필 수정
            else:
                if password:
                    user.set_password(password)
                user.nickname = nickname if nickname else user.nickname
                user.introduce = introduce if introduce else user.introduce
                user.save()
                context = {'success': '수정이 완료되었습니다.'}
                return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        message = '자신의 프로필만 수정할 수 있습니다.'
    context ={'message': message}
    return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def follow(request, username):
    user = get_user_model()
    me = request.user
    you = get_object_or_404(user, username=username)
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
