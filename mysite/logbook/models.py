from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Movie(models.Model):
    name = models.CharField(max_length=30)
    year = models.DateField()
    stars = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)])
    descriptions = models.TextField(max_length=800)

    def __str__(self):
        return f"Name: {self.name}"


class Cinema(models.Model):
    name = models.CharField(max_length=30)
    descriptions = models.TextField(max_length=800)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=60)

    def __str__(self):
        return f"Name: {self.name}"

class CinemaUser(models.Model):
    cinema_id = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Hall(models.Model):
    room = models.IntegerField()
    cinema_id = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    seats = models.IntegerField()
    volume = models.CharField(max_length=3)


class Session(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall_id = models.ForeignKey(Hall, on_delete=models.CASCADE)
    price = models.IntegerField()
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()