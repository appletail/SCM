from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='login'),
    path('<str:username>/', views.profile, name='profile'),
    path('<str:username>/update/', views.update, name='update'),
    # path('<str:username>/follow/', views.follow, name='follow'),
    path('<str:username>/<str:page_name>/', views.follow, name='follow'),
]
