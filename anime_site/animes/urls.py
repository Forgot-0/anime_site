from django.urls import path
from .views import AnimeListView, AnimeDetailView, EpisodeDetailView, random_anime


urlpatterns = [
    path('random/', random_anime, name='random_anime'),
    path('', AnimeListView.as_view(), name='anime_list'),
    path('<slug:slug>/', AnimeDetailView.as_view(), name='anime_detail'),
    path('<str:title>/<str:season>/', EpisodeDetailView.as_view(), name='episode_detail'),
]
