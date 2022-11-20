from django.urls import path
from . import views

urlpatterns = [
    path('<str:reviews_filter>/',views.reviews_list),
    # path('create/',views.reviews_create),
    path('<int:review_pk>',views.reviews_detail),
    path('comments/',views.reviewscomments_list),
    path('<int:review_pk>/reviewscomments/',views.reviewscomments_create),
    path('comments/<int:comment_pk>/',views.reviewscomments_detail)
]
