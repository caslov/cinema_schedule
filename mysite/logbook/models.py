from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Cinema(models.Model):
    name = models.CharField(max_length=30)
    descriptions = models.TextField(max_length=800)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=60)


class Hall(models.Model):
    room = models.IntegerField()
    cinema_id = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    seats = models.IntegerField()
    volume = models.CharField(max_length=3)


class Movie(models.Model):
    name = models.CharField(max_length=30)
    year = models.DateField()
    stars = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)])
    descriptions = models.TextField(max_length=800)
    pictures = models.TextField(max_length=800)


class Session(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall_id = models.ForeignKey(Hall, on_delete=models.CASCADE)
    price = models.IntegerField()
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, default="administrator")
    cinema_id = models.ForeignKey(Cinema, on_delete=models.CASCADE)