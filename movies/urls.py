from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # path('<int:movie_pk>/wordcloud/', views.wordcloud_upload, name='wordcloud_upload'),
    path('<int:movie_pk>/want/', views.want, name='want'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    path('', views.home, name='home'),
]
