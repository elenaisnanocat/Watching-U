from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('<int:review_pk>/like/', views.like, name='like'),
    path('<int:review_pk>/comments/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'), 
    path('<int:review_pk>/comments/', views.create_comment, name='create_comment'),
    path('<int:review_pk>/delete/', views.delete, name='delete'),
    path('<int:review_pk>/update/', views.update, name='update'),
    path('<int:movie_pk>/create/', views.create, name='create'),
    path('<int:review_pk>/', views.detail, name='detail'),
    path('', views.index, name='index'),
]