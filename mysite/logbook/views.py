from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import (Movie,
                     Cinema,
                     Hall,
                     Session,
                     CinemaUser)


# Movie
class MovieCreate(CreateView):
    model = Movie
    fields = ['id', "name", "year", "stars", "descriptions"]
    success_url = "list/"
    template_name = 'movie/movie_create.html'


class MovieList(ListView):
    model = Movie
    template_name = 'movie/movie_list.html'


class MovieDetail(DetailView):
    model = Movie
    queryset = Movie.objects
    success_url = "list/"
    template_name = 'movie/movie_detail.html'


class MovieUpdate(UpdateView):
    model = Movie
    fields = ['id', "name", "year", "stars", "descriptions"]
    success_url = "list/"
    template_name = 'movie/movie_update.html'


class MovieDelete(DeleteView):
    model = Movie
    success_url = "list/"
    template_name = 'movie/movie_delete.html'


# cinemaUser
class CinemaUserCreate(CreateView):
    model = CinemaUser
    fields = ['id', "cinema_id", "user_id"]
    success_url = "list/"
    template_name = 'cinemaUser/cinema_user_create.html'


class CinemaUserList(ListView):
    model = CinemaUser
    template_name = 'cinemaUser/cinema_user_list.html'


class CinemaUserDetail(DetailView):
    model = CinemaUser
    queryset = CinemaUser.objects
    success_url = "list/"
    template_name = 'cinemaUser/cinema_user_detail.html'


class CinemaUserUpdate(UpdateView):
    model = CinemaUser
    fields = ["'id', cinema_id", "user_id"]
    success_url = "list/"
    template_name = 'cinemaUser/cinema_user_update.html'


class CinemaUserDelete(DeleteView):
    model = CinemaUser
    success_url = "list/"
    template_name = 'cinemaUser/cinema_user_delete.html'


# cinema
class CinemaCreate(CreateView):
    model = Cinema
    fields = ['id', "name", "descriptions", "city", "address"]
    success_url = "list/"
    template_name = 'cinema/cinema_create.html'


class CinemaList(ListView):
    model = Cinema
    template_name = 'cinema/cinema_list.html'


class CinemaDetail(DetailView):
    model = Cinema
    queryset = Cinema.objects
    success_url = "list/"
    template_name = 'cinema/cinema_detail.html'


class CinemaUpdate(UpdateView):
    model = Cinema
    fields = ['id', "name", "descriptions", "city", "address"]
    success_url = "list/"
    template_name = 'cinema/cinema_update.html'


class CinemaDelete(DeleteView):
    model = Cinema
    success_url = "list/"
    template_name = 'cinema/cinema_delete.html'


# hill
class HallCreate(CreateView):
    model = Hall
    fields = ['id', "room", "cinema_id", "seats", "volume"]
    success_url = "list/"
    template_name = 'hill/hill_create.html'


class HallList(ListView):
    model = Hall
    template_name = 'hill/hill_list.html'


class HallDetail(DetailView):
    model = Hall
    queryset = Hall.objects
    template_name = 'hill/hill_detail.html'


class HallUpdate(UpdateView):
    model = Hall
    fields = ['id', "room", "cinema_id", "seats", "volume"]
    success_url = "list/"
    template_name = 'hill/hill_update.html'


class HallDelete(DeleteView):
    model = Hall
    success_url = "list/"
    template_name = 'hill/hill_delete.html'


# Session
class SessionCreate(CreateView):
    model = Session
    fields = ['id', "movie_id", "hall_id", "price", "time_start", "time_end"]
    template_name = 'session/session_create.html'
    success_url = "list/"


class SessionList(ListView):
    model = Session
    template_name = 'session/session_list.html'


class SessionDetail(DetailView):
    model = Session
    queryset = Session.objects
    template_name = 'session/session_detail.html'


class SessionUpdate(UpdateView):
    model = Session
    fields = ['id', "movie_id", "hall_id", "price", "time_start", "time_end"]
    template_name = 'session/session_update.html'
    success_url = "list/"


class SessionDelete(DeleteView):
    model = Session
    success_url = "session/list/"
    template_name = 'session/session_delete.html'
    success_url = "list/"