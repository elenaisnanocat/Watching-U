from django.db import models
from django.conf import settings
from django.db.models import Q

# Create your models here.
class SearchManager(models.Manager):
    def search(self, **kwargs):
        qs = self.get_queryset()

        movie = kwargs.get('movie')
        qs = qs.filter(
            Q(title__icontains=movie) | Q(director__icontains=movie)
        )

        return qs


class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    want_users = models.ManyToManyField(settings.AUTH_USER_MODEL, symmetrical=False, related_name='want_movies')
    genres = models.ManyToManyField(Genre, symmetrical=False, related_name='movie')
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField()
    popularity = models.FloatField()
    vote_average = models.FloatField()
    poster_path = models.CharField(max_length=200)
    backdrop_path = models.CharField(max_length=200, null=True)
    actors = models.TextField(blank=True)
    director = models.CharField(max_length=50, null=True)
    runtime = models.IntegerField(null=True)
    wordcloud = models.ImageField(blank=True)
    objects = SearchManager()

    def __str__(self):
        return f'[{self.title}]'