from django.urls import path
from users.views import UserDetailView, UserView
from rest_framework_simplejwt import views


urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/login/", views.TokenObtainPairView.as_view()),
    path("users/<user_id>/", UserDetailView.as_view()),
]
