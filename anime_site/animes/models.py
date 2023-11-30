from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from files.models import Video, Picture
from reactions.models import Reactions
# from stream_videos.models import Video


def anime_image_path(instance, filename):
    return f'anime/{instance.title}/{filename}'

def anime_background_path(instance, filename):
    return f'anime/{instance.title}/{filename}'

def pictures_anime_path(instance, filename):
    return f'anime/{instance.anime.title}/{filename}'

def episode_poster_path(instance, filename):
    return f'anime/poster/{instance.title}/{filename}'


# Create your models here.
class Anime(Reactions):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, primary_key=True)

    description = models.TextField()
    image = models.ImageField(upload_to=anime_image_path)
    views = models.IntegerField(default=0)

    genres = models.ManyToManyField('Tag', related_name='genre')
    topics = models.ManyToManyField('Tag', related_name='topic')

    years = models.ManyToManyField('Year')

    background = models.FileField(upload_to=anime_background_path)

    imgs = GenericRelation(Picture, object_id_field='object_pk')

    def __str__(self) -> str:
        return self.slug
    

class Season(models.Model):
    title = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40, unique=True, primary_key=True)
    count_series = models.IntegerField()
    anime = models.ForeignKey('Anime', on_delete=models.CASCADE, related_name='seasons')

    prev = models.ForeignKey("Season", on_delete=models.CASCADE, null=True, blank=True, related_name='previous')
    next = models.ForeignKey("Season", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.slug


class Episode(models.Model):
    title = models.CharField(max_length=20)
    nomer = models.PositiveIntegerField(blank=True, null=True)
    season = models.ForeignKey('Season', on_delete=models.CASCADE, related_name='episodes')
    poster = models.ImageField(upload_to=episode_poster_path)


    video = GenericRelation(Video, object_id_field='object_pk')

    def __str__(self) -> str:
        return self.title


class Tag(models.Model):
    slug = models.SlugField(unique=True, primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name
    

class Year(models.Model):
    slug = models.SlugField(unique=True, primary_key=True)
    name = models.PositiveSmallIntegerField(default=0)

    def __str__(self) -> str:
        return str(self.name)