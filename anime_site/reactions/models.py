from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Reaction(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True, primary_key=True)

    def __str__(self):
        return self.name


class UserReaction(models.Model):
    reaction = models.ForeignKey("Reaction", on_delete=models.CASCADE)

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='reactions',
                             on_delete=models.PROTECT)

    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_pk = models.SlugField()
    content_object = GenericForeignKey('content_type', 'object_pk')

    def __str__(self) -> str:
        return f'{self.user} {self.reaction}: {self.content_object}'


class TotalReaction(models.Model):
    name = models.ForeignKey('Reaction', on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_pk = models.SlugField()
    content_object = GenericForeignKey('content_type', 'object_pk')

    total = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f'{self.name}-{self.content_type}'


class Reactions(models.Model):
    reactions = GenericRelation(UserReaction, object_id_field='object_pk')
    total_reacs = GenericRelation(TotalReaction, object_id_field='object_pk')

    class Meta:
        abstract = True
