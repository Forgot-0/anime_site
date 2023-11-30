from django.db import models
from animes.models import Anime
from django.contrib.contenttypes.fields import GenericRelation
from reactions.models import UserReaction
from files.models import Audio, Picture
from reactions.models import Reactions

# Create your models here.
class Person(Reactions):
    title = models.CharField(max_length=25)
    slug = models.SlugField(max_length=25, unique=True, primary_key=True)

    avatar = models.ImageField(upload_to='anime/avatarka/', blank=True)
    description = models.TextField()

    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, to_field='slug')

    imgs = GenericRelation(Picture, object_id_field='object_pk')
    voices = GenericRelation(Audio, object_id_field='object_pk')

    def __str__(self) -> str:
        return f'{self.title}'
