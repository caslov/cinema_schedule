from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('movie/create/', MovieCreate.as_view()),
    path('movie/<int:pk>/', MovieDetail.as_view()),
    path('movie/list/', MovieList.as_view()),
    path('movie/<int:pk>/update/', MovieUpdate.as_view()),
    path('movie/<int:pk>/delete/', MovieDelete.as_view()),
]