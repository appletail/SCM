from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.reviews_create),
    path('latest/',views.reviews_list_latest),
    path('popular/',views.reviews_list_popular),
    path('view/',views.reviews_list_view),
    path('<int:review_pk>/',views.reviews_detail),
    path('<int:review_pk>/review_like/', views.review_like),
    path('<int:review_pk>/lookup/',views.review_lookup),
    path('comments/',views.reviewscomments_list),
    path('<int:review_pk>/reviewscomments/',views.reviewscomments_create),
    path('comments/<int:comment_pk>/',views.reviewscomments_detail),
]
