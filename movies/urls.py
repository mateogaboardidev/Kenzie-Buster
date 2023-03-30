from django.urls import path
from movies.views import MovieView, MovieDetailView, MovieOrderView
from rest_framework_simplejwt import views


urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<int:movie_id>/", MovieDetailView.as_view()),
    path("movies/<int:movie_id>/orders/", MovieOrderView.as_view()),
]
