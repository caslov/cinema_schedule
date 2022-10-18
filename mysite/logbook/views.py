from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView


from .models import (Movie,
                     Cinema,
                     Hall,
                     Session,
                     CinemaUser)


from .forms import (MovieForm,
                    CinemaForm,
                    HallForm,
                    SessionForm,
                    CinemaUserForm)


# Movie
class MovieListView(ListView):
    model = Movie
    template_name = 'movies.html'


class Movie(DetailView):
    model = Movie
    template_name = 'movie.html'
    queryset = Movie.objects


class MovieCreate(CreateView):
    model = MovieForm
    fields = ["name", "year", "stars", "descriptions", "pictures"]





# CinemaUser
class CinemaUserListView(ListView):
    model = CinemaUser
    template_name = 'list_cinema_user.html.html'


class CinemaUser(DetailView):
    model = Cinema
    template_name = 'cinema_user.html.html'
    queryset = CinemaUser.objects


def create_cinema_user(request):
    if request.method == "POST":
        form = CinemaUserForm(request.POST)
        if form.is_valid():
            cinema = form.save(commit=False)
            cinema.user = request.user
            cinema.save()
    form = CinemaUserForm()
    return render(request, 'create_cinema_user.html', {'form': form})


# Cinema
class CinemaListView(ListView):
    model = Cinema
    template_name = 'cinema.html'


class Cinema(DetailView):
    model = Cinema
    template_name = 'cinemas.html'
    queryset = Cinema.objects


def create_сinema(request):
    if request.method == "POST":
        form = CinemaForm(request.POST)
        if form.is_valid():
            cinema = form.save(commit=False)
            cinema.user = request.user
            cinema.save()
    form = CinemaForm()
    return render(request, '.html', {'form': form})




# Hall
def get_all_hall(request):
    all_hall = Hall.objects.all()
    return HttpResponse(all_hall)


def get_hall_by_id(request, id):
    return get_object_or_404(Hall, pk=id)


def create_hall(requst):
    form = HallForm(requst.POST)
    if form.is_valid():
        try:
            st = Hall.objects.create(
                room=form.cleaned_data['room'],
                cinema_id=form.cleaned_data['cinema_id'],
                seats=form.cleaned_data['seats'],
            )
        except: pass
    return get_object_or_404(st)


# Session
def get_all_Session(request):
    all_Session = Session.objects.all()
    return HttpResponse(all_Session)


def get_Session_by_id(request, id):
    return get_object_or_404(Session, pk=id)


def create_Session(requst):
    form = SessionForm(requst.POST)
    if form.is_valid():
        try:
            st = Session.objects.create(
                movie_id=form.cleaned_data['movie_id'],
                hall_id=form.cleaned_data['hall_id'],
                price=form.cleaned_data['price'],
                time_start=form.cleaned_data['time_start'],
                time_end=form.cleaned_data['time_end'],
            )
        except: pass
    return get_object_or_404(st)

