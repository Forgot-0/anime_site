from rest_framework.permissions import IsAuthenticatedOrReadOnly
from animes.models import Anime, Season, Episode, Tag
from .serializers import AnimeDetailSerializer, AnimeSerializer, SeasonSerializer, TagSerializer, EpisodeSerializer
from reactions.api.mixins import ReactiondMixin
from files.api.mixins import FileMixin
from comments.api.mixins import CommentMixin
from mixins.viewsets import CustomModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissions
from django_filters.rest_framework import DjangoFilterBackend


class AnimeViewSet(CommentMixin, ReactiondMixin, CustomModelViewSet):
    queryset = Anime.objects.prefetch_related('genres', 'topics', 'years').all()
    # permission_classes = (DjangoModelPermissions,)
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ('genres', 'topics', 'years')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AnimeDetailSerializer
        return AnimeSerializer


class SeasonViewSet(CustomModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    # permission_classes = (DjangoModelPermissions, )


class EpisodeViewSet(CustomModelViewSet, FileMixin):
    queryset = Episode.objects.prefetch_related('video').all()
    serializer_class = EpisodeSerializer
    # permission_classes = (DjangoModelPermissions,)
    
    def list(self, request, *args, **kwargs):
        return Response({"list": "Method \"GET\" not allowed."})


class TagViewSet(CustomModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # permission_classes = (DjangoModelPermissions,)

