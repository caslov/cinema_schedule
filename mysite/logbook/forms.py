from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import (Movie,
                     Cinema,
                     Hall,
                     Session)


# Movie:
#  name
#  year
#  stars
#  descriptions
#  pictures


class MovieForm(forms.Form):
    class Meta:
        cinema = Movie
        fields = ("name", "year", "stars", "descriptions", "pictures")



# Cinema:
#  name
#  descriptions
#  city
#  address


class CinemaForm(forms.Form):
    class Meta:
        cinema = Cinema
        fields = ("name", "year", "stars", "descriptions", "pictures")



# Admin:
#  user
#  role
#  cinema_id


#class AdminForm(ModelForm):
#    class Meta:
#        cinema = Admin
#        fields = ["name"]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

#  Hall
# room
# cinema_id
# seats
# volume


class HallForm(forms.Form):
    class Meta:
        cinema = Hall
        fields = ("room", "cinema_id", "seats", "volume")


# Session:
#  movie_id
#  hall_id
#  price
#  time_start
#  time_end


class SessionForm(forms.Form):
    class Meta:
        movie = Session
        fields = ["movie_id", "hall_id", "price", "time_start", "time_end"]


# https://stackoverflow.com/questions/31130706/dropdown-in-django-model