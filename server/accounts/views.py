from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer

# Create your views here.

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    password = request.data.get('password')
    password_confirm = request.data.get('password_confirm')
    nickname = request.data.get('nickname')

    if password != password_confirm:
        data = {'password_unmatch': '비밀번호가 일치하지 않습니다.',}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(password)
        user.nickname = nickname if nickname else user.username
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def profile(request, username):
    profile_user = get_object_or_404(get_user_model(), username=username)
    if request.method == 'GET':
        context = {
            'username': profile_user.username,
            'nickname': profile_user.nickname,
            'introduce': profile_user.introduce,
        }
        return Response(context)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        profile_user.delete()