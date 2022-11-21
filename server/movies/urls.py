from django.urls import path
from . import views

urlpatterns = [
    path('',views.movies_list),
    path('popular/',views.movies_list_popular),
    path('personal/',views.movies_list_personal),
    path('latest/',views.movies_list_latest),
    # path('upcoming/',views.movies_list_upcoming),
    path('<int:movie_pk>/',views.movies_detail),
    path('crews/actor/',views.crews_list),
    path('crews/director/',views.director_list),
    path('crews/<int:crew_pk>/',views.crews_detail),
    path('makeDB/',views.makedb),
]
