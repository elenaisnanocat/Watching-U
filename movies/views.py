from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET, require_POST, require_http_methods, require_safe
from .models import Genre, Movie


# Create your views here.



def home(request):
    movies = Movie.objects.order_by('-release_date')
    context = {
        'movies': movies
    }
    return render(request, 'movies/home.html', context)


def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie':movie
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