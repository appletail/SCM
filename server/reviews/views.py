from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from movies.models import Movie
from .models import Review, ReviewComment
from .serializers import ReviewListSerializer, ReviewCommentSerializer, ReviewSerializer, ReviewCreateSerializer
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
# Create your views here.

# 최신순 정렬
@api_view(['GET'])
def reviews_list_latest(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        reviews = sorted(reviews, key = lambda x: x.created_at, reverse=True)
        # 정렬된 데이터 조회
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)


# 인기순 정렬
@api_view(['GET'])
def reviews_list_popular(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        # 정렬된 데이터 조회
        serializer = ReviewListSerializer(reviews, many=True)
        popular_reviews = sorted(serializer.data, key= lambda x: x.get('like_users_count'), reverse=True)
        return Response(popular_reviews)


# 조회순 정렬
@api_view(['GET'])
def reviews_list_view(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        reviews = sorted(reviews, key= lambda x: x.Lookup_cnt, reverse=True)
        # 정렬된 데이터 조회
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def reviews_create(request):
    # 전체 데이터 조회인데 일단 적었습니다.
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ReviewCreateSerializer(data=request.data)
        movie = Movie.objects.get(pk=request.data.get('movie').get('id'))

        if serializer.is_valid(raise_exception=True):
            review = serializer.save(movie=movie)
            review.user = request.user
            review.save()
        return Response(status=status.HTTP_201_CREATED)


@api_view(['GET','DELETE','PUT'])
def reviews_detail(request,review_pk):
    review = Review.objects.get(pk=review_pk)

    # 리뷰 상세 조회
    if request.method == 'GET': 
        serializer = ReviewSerializer(review)
        if request.user.pk in serializer.data.get('like_users'):
            like = '좋아요 취소'
        else:
            like = '좋아요'
        context = { 'reviewLike': like }
        context.update(serializer.data)
        return Response(context)
    
    # 리뷰 삭제
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # 리뷰 수정
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

''' 
댓글 
'''

# 리뷰 전체 댓글 조회
@api_view(['GET'])
def reviewscomments_list(request):
    if request.method == 'GET':
        comments = ReviewComment.objects.all()
        serializer = ReviewCommentSerializer(comments, many=True)
        return Response(serializer.data)


# 리뷰 댓글 생성
@api_view(['POST'])
def reviewscomments_create(request,review_pk):
    review = Review.objects.get(pk=review_pk)
    serializer = ReviewCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        comment = serializer.save(review=review)
        comment.user = request.user
        comment.save()
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


@api_view(['POST'])
def review_like(request, review_pk):
    me = request.user
    review = Review.objects.get(pk=review_pk)

    if request.method == 'POST':
        if review.like_users.filter(username=me.username).exists():
            review.like_users.remove(me)
            message = '좋아요'
        else:
            # 팔로우
            review.like_users.add(me)
            message = '좋아요 취소'
        context = {'message': message,}
        return Response(context, status=status.HTTP_200_OK)


@api_view(['POST'])
def review_lookup(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    review.Lookup_cnt += 1
    review.save()
    return Response(status=status.HTTP_200_OK)
