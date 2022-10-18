from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import (Movie,
                     Cinema,
                     Hall,
                     Session,
                     CinemaUser)


# Movie
class MovieCreate(CreateView):
    model = Movie
    fields = ["name", "year", "stars", "descriptions", "pictures"]
    template_name = 'movie_create.html'


class MovieList(ListView):
    model = Movie
    template_name = 'movie_list.html'


class MovieDetail(DetailView):
    model = Movie
    queryset = Movie.objects
    template_name = 'movie_detail.html'


class MovieUpdate(UpdateView):
    model = Movie
    fields = ["name", "year", "stars", "descriptions", "pictures"]
    template_name = 'movie_update.html'


class MovieDelete(DeleteView):
    model = Movie
    success_url = "/"
    template_name = 'movie_delete.html'


# CinemaUser
class CinemaUserCreate(CreateView):
    model = CinemaUser
    fields = ["cinema_id", "user_id"]
    template_name = 'cinema_user_create.html'


class CinemaUserList(ListView):
    model = CinemaUser
    template_name = 'cinema_user_list.html'


class CinemaUserDetail(DetailView):
    model = CinemaUser
    queryset = CinemaUser.objects
    template_name = 'cinema_user_detail.html'


class CinemaUserUpdate(UpdateView):
    model = CinemaUser
    fields = ["cinema_id", "user_id"]
    template_name = 'cinema_user_update.html'


class CinemaUserDelete(DeleteView):
    model = CinemaUser
    success_url = "/"
    template_name = 'cinema_user_delete.html'


# Cinema
class CinemaCreate(CreateView):
    model = Cinema
    fields = ["name", "descriptions", "city", "address"]
    template_name = 'cinema_create.html'


class CinemaList(ListView):
    model = Cinema
    template_name = 'cinema_list.html'


class CinemaDetail(DetailView):
    model = Cinema
    queryset = Cinema.objects
    template_name = 'cinema_detail.html'


class CinemaUpdate(UpdateView):
    model = Cinema
    fields = ["name", "descriptions", "city", "address"]
    template_name = 'cinema_update.html'


class CinemaDelete(DeleteView):
    model = Cinema
    success_url = "/"
    template_name = 'cinema_delete.html'


# Hall
class HallCreate(CreateView):
    model = Hall
    fields = ["room", "cinema_id", "seats", "volume"]
    template_name = 'hill_create.html'


class HallList(ListView):
    model = Hall
    template_name = 'hill_list.html'


class HallDetail(DetailView):
    model = Hall
    queryset = Hall.objects
    template_name = 'hill_detail.html'


class HallUpdate(UpdateView):
    model = Hall
    fields = ["room", "cinema_id", "seats", "volume"]
    template_name = 'hill_update.html'


class HallDelete(DeleteView):
    model = Hall
    success_url = "/"
    template_name = 'hill_delete.html'


# Session
class SessionCreate(CreateView):
    model = Session
    fields = ["movie_id", "hall_id", "price", "time_start", "time_end"]
    template_name = 'session_create.html'


class SessionList(ListView):
    model = Session
    template_name = 'session_list.html'


class SessionDetail(DetailView):
    model = Session
    queryset = Session.objects
    template_name = 'session_detail.html'


class SessionUpdate(UpdateView):
    model = Session
    fields = ["movie_id", "hall_id", "price", "time_start", "time_end"]
    template_name = 'session_update.html'


class SessionDelete(DeleteView):
    model = Session
    success_url = "/"
    template_name = 'session_delete.html'
