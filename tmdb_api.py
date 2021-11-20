import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "watchingu.settings")

import django
django.setup()

import requests
import json

from movies.models import Genre, Movie

API_KEY = '5d898d026f62971327395d0f2504eef7'
API_URL = 'https://api.themoviedb.org/3'

language = 'ko-KR'
region = 'KR'

## runtime
def get_detail_credits(movie_id):

    detail_url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language={language}'
    detail_response = requests.get(detail_url).json()
    
    credits_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}&language={language}'
    credits_response = requests.get(credits_url).json()


    runtime = detail_response['runtime']

    director = None
    for crew in credits_response['crew']:
        if crew['job'] == 'Director':
            director = crew['name']
            break

    actors = [cast['name'] for cast in credits_response['cast']][:10]


    context = {
        'director': director,
        'actors': actors,
        'runtime': runtime
    }
    return context

## 장르 
# genre_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language={language}'
# genre_response = requests.get(genre_url).json().get('genres')

# print(genre_response)

# for gr in genre_response:
#     genre = Genre()
#     genre.id = gr['id']
#     genre.name = gr['name']
#     genre.save()


# # 영화
for i in range(1, 2):
    movie_url = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language={language}&page={i}'
    movie_response = requests.get(movie_url).json().get('results')

    # print(movie_response)

    for mv in movie_response:
        movie = Movie()
        movie.movie_id = mv['id']
        movie.title = mv['title']
        movie.overview = mv['overview']
        movie.release_date = mv['release_date']
        movie.popularity = mv['popularity']
        movie.vote_average = mv['vote_average']
        movie.poster_path = 'https://image.tmdb.org/t/p/original' + mv['poster_path']
        movie.backdrop_path = 'https://image.tmdb.org/t/p/original' + mv['backdrop_path']
        movie.director = get_detail_credits(mv['id'])['director']
        movie.actors = get_detail_credits(mv['id'])['actors']
        movie.runtime = get_detail_credits(mv['id'])['runtime']
        movie.save()
        for genre_id in mv['genre_ids']:
            movie.genres.add(genre_id)