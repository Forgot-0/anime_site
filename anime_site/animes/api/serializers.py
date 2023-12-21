from rest_framework import serializers
from reactions.api.mixins import ReactionMixinSerializer
from animes.models import Anime, Season, Episode, Tag, Year
from files.api.serializers import VideoListDetailSerializer
from comments.api.serializers import ComentSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', 'slug')


class AnimeSerializer(ReactionMixinSerializer, serializers.ModelSerializer):
    genres_pk = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), source='genres', write_only=True, many=True)
    topics_pk = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), source='topics', write_only=True, many=True)
    years_pk = serializers.PrimaryKeyRelatedField(
        queryset=Year.objects.all(), source='years', write_only=True, many=True)
    
    class Meta:
        model = Anime
        fields = (
            'title',
            'slug',
            'description',
            'image',
            'background',
            'genres',
            'genres_pk',
            'topics',
            'topics_pk',
            'years',
            'years_pk',
            'is_react'
            )
        depth = 1
        

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'


class SeasonDetailSerializer(serializers.ModelSerializer):
    episodes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Season
        fields = (
            'title',
            'slug',
            'count_series', 
            'episodes'
        )



class EpisodeSerializer(serializers.ModelSerializer):
    video = VideoListDetailSerializer(many=True, read_only=True)
    
    class Meta:
        model = Episode
        fields = (
            'title',
            'nomer',
            'poster',
            'video',
            )


class AnimeDetailSerializer(ReactionMixinSerializer, serializers.ModelSerializer):
    seasons = SeasonDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Anime
        fields = (
            'title',
            'slug',
            'description',
            'image',
            'background',
            'is_react',
            'genres',
            'topics',
            'years',
            'seasons'
            )
        depth = 1