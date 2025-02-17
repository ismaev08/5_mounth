from django.urls import path
from . import views

urlpatterns = [
    path('directors/', views.director_list, name='director_list'),
    path('directors/<int:id>/', views.director_detail, name='director_detail'),
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:id>/', views.movie_detail, name='movie_detail'),
    path('reviews/', views.review_list, name='review_list'),
    path('reviews/<int:id>/', views.review_detail, name='review_detail'),
]