from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('movies/create/', MovieCreate.as_view()),
    path('movies/<int:pk>/', MovieDetail.as_view()),
    path('movies/List/', MovieList.as_view()),
    path('movies/<int:pk>/update', MovieUpdate.as_view()),
    path('movies/<int:pk>/delete/', MovieDelete.as_view()),
]