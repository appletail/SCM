from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Review, ReviewComment
from .serializers import ReviewListSerializer, ReviewCommentSerializer, ReviewSerializer
from django.shortcuts import get_object_or_404, get_list_or_404
# Create your views here.
@api_view(['GET','POST'])
def reviews_list(request,reviews_filter):
    if request.method == "POST":
        if reviews_filter == 'create':
            print('이건 실행됩니다.')
            # print(request.user)
            # 디버깅용
            for _ in range(10):
                print(' ')
            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    if request.method == 'GET':
        # reviews = Review.objects.all()
        reviews = get_list_or_404(Review)

        if reviews_filter == 'latest':
            reviews = sorted(reviews, key = lambda x: x.created_at)

        elif reviews_filter == 'popular':
            reviews = sorted(reviews, key = lambda x: len(x.like_users))

        elif reviews_filter == 'view':
            reviews = sorted(reviews, key= lambda x: x.Lookup_cnt, reverse=True)

        # 정렬된 데이터 조회
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)



# @api_view(['GET', 'POST'])
# def reviews_create(request):
#     # # 전체 데이터 조회인데 일단 적었습니다.
#     # if request.method == 'GET':
#     #     reviews = Review.objects.all()
#     #     serializer = ReviewListSerializer(reviews, many=True)
#     #     return Response(serializer.data)
    
#     # elif request.method == 'POST':
#     serializer = ReviewSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(user=request.user)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','DELETE','PUT'])
def reviews_detail(request,review_pk):
    review = Review.objects.get(pk=review_pk)

    # 리뷰 상세 조회
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    # 리뷰 삭제
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# 리뷰 전체 댓글 조회
@api_view(['GET'])
def reviewscomments_list(request):
    if request.method == 'GET':
        comments = ReviewComment.objects.all()
        serializer = ReviewListSerializer(comments, many=True)
        return Response(serializer.data)

# 리뷰 댓글 생성
@api_view(['POST'])
def reviewscomments_create(request,review_pk):
    review = Review.objects.get(pk=review_pk)
    serializer = ReviewCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 리뷰 댓글 상세 조회, 삭제, 수정
@api_view(['GET', 'DELETE', 'PUT'])
def reviewscomments_detail(request,comment_pk):
    comment = ReviewComment.objects.get(pk=comment_pk)

    if request.method == 'GET':
        serializer = ReviewCommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewCommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
