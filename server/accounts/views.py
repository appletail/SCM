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
