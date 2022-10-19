from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('movie/create/', MovieCreate.as_view()),
    path('movie/<int:pk>/', MovieDetail.as_view()),
    path('movie/list/', MovieList.as_view()),
    path('movie/<int:pk>/update/', MovieUpdate.as_view()),
    path('movie/<int:pk>/delete/', MovieDelete.as_view()),

    path('cinemaUser/create/', CinemaUserCreate.as_view()),
    path('cinemaUser/<int:pk>/', CinemaUserDetail.as_view()),
    path('cinemaUser/list/', CinemaUserList.as_view()),
    path('cinemaUser/<int:pk>/update/', CinemaUserUpdate.as_view()),
    path('cinemaUser/<int:pk>/delete/', CinemaUserDelete.as_view()),

    path('cinema/create/', CinemaCreate.as_view()),
    path('cinema/<int:pk>/', CinemaDetail.as_view()),
    path('cinema/list/', CinemaList.as_view()),
    path('cinema/<int:pk>/update/', CinemaUpdate.as_view()),
    path('cinema/<int:pk>/delete/', CinemaDelete.as_view()),

    path('hill/create/', HallCreate.as_view()),
    path('hill/<int:pk>/', HallDetail.as_view()),
    path('hill/list/', HallList.as_view()),
    path('hill/<int:pk>/update/', HallUpdate.as_view()),
    path('hill/<int:pk>/delete/', HallDelete.as_view()),

    path('session/create/', SessionCreate.as_view()),
    path('session/<int:pk>/', SessionDetail.as_view()),
    path('session/list/', SessionList.as_view()),
    path('session/<int:pk>/update/', SessionUpdate.as_view()),
    path('session/<int:pk>/delete/', SessionDelete.as_view()),
]