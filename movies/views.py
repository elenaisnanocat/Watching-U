from django.db.models.aggregates import Count, Max
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.views.decorators.http import require_GET, require_POST, require_http_methods, require_safe
from .models import Genre, Movie
from django.db.models import Avg
import random


# Create your views here.



def home(request):
    movies = Movie.objects.order_by('-release_date')
    context = {
        'movies': movies
    }
    return render(request, 'movies/home.html', context)



def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if '[' and ']' in movie.actors:
            actors = eval(movie.actors)
            
    comments_cnt = movie.review_set.count()
    if comments_cnt != 0:
        rank = movie.review_set.all().aggregate(Avg('rank'))
        averages = rank['rank__avg']
        average = int(averages)
        
        context = {
            'comments_cnt': comments_cnt,
            'movie':movie,
            'average': average,
            'actors':actors
    }
    else:
        context = {
            'comments_cnt': comments_cnt,
            'movie':movie,
            'actors':actors
        }
    return render(request, 'movies/detail.html', context)



@require_POST
def want(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user

        if movie.want_users.filter(pk=user.pk).exists():
            movie.want_users.remove(user)
            is_want = False
        else:
            movie.want_users.add(user)
            is_want = True
        
        data = {
            'is_want': is_want,
            'cnt_want': movie.want_users.count(),
        }
        return JsonResponse(data)
    return HttpResponse(status=401)


@require_safe
def search(request):
    keyword = request.GET.get('keyword', default="")
    movies = Movie.objects.search(movie=keyword)
    context = {
        'keyword': keyword,
        'movies': movies, 
    }
    return render(request, 'movies/search_result.html', context)


@require_safe
def recommend(request):
    movies = Movie.objects.all()
    genre_pick = None
    genre_movies = None
    following_movies = []
    directors = []
    director_lst = []
    director_movies = []
    if request.user.is_authenticated:
        user = request.user
        # 선호 장르 
        if user.review_set.all():
            review = user.review_set.order_by('-rank')[0]
            genres = review.movie.genres.all()

            genre_lst = []
            for genre in genres:
                genre_lst.append(genre)

            genre_pick = random.choice(genre_lst)
            genre_movies = Movie.objects.filter(genres=genre_pick)
                

        # 선호 감독
        # user_movies = []
        # if user.review_set:
        #     for review in user.review_set.all():
        #         user_movies.append(review.movie)
        #         directors.append(review.movie.director)
        # if user.want_movies:
        #     user_movies.extend(user.want_movies.all())
        #     for movie in user.want_movies.all():
        #         directors.append(movie.director)
        # for director in directors:
        #     if Movie.objects.filter(director = director):
        #         if Movie.objects.filter(director = director) in user_movies:
        #             break
        #         director_lst.append(director)
        #         director_movies.append(Movie.objects.filter(director = director))
            

        # 팔로우 
        if user.followings.all():
            followings = user.followings.all()
            for following in followings:
                if following.review_set.all().count() != 0:
                    review = following.review_set.order_by('-rank')[0]
                    following_movies.append(review.movie)

        
        want_movies = Movie.objects.order_by('want_users')

    context = {
        'movies':movies,
        'genre_pick': genre_pick,
        'genre_movies': genre_movies,
        'following_movies': following_movies,
        'director_lst': director_lst,
        'directors': directors,
        'want_movies': want_movies
    }
    return render(request, 'movies/recommend.html', context)