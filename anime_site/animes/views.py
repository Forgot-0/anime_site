from random import randint
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from .models import Anime, Episode

# Create your views here.
class AnimeListView(ListView):
    model = Anime
    template_name = 'anime/anime_list.html'
    context_object_name = 'animes'
    paginate_by = 20

    def get_queryset(self):
        if self.request.GET:
            return Anime.objects.prefetch_related('genres').prefetch_related('imgs')
        return Anime.objects.all().prefetch_related('genres').prefetch_related('imgs')


class AnimeDetailView(DetailView):
    model = Anime
    template_name = 'anime/anime_detail.html'
    context_object_name = 'anime'


class EpisodeDetailView(ListView):
    model = Episode
    template_name = 'anime/episode_detail.html'
    context_object_name = 'episode'
    paginate_by = 1
    page_kwarg = 'episode'

    def get_queryset(self):
        return Episode.objects.filter(season__slug=self.kwargs['season']).prefetch_related('video')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['episode'] = data['episode'][0]
        data['anime'] = data['episode'].season.anime
        data['season'] = data['episode'].season
        data['anime_slug'] = self.kwargs['title']
        data['season_slug'] = self.kwargs['season']
        return data


def random_anime(request):
    anime = Anime.objects.all()[randint(0, Anime.objects.count()-1)]
    return redirect('anime_detail', slug=anime.slug)