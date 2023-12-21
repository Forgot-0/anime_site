from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from reactions.models import Reactions


# Create your models here.
class Comment(Reactions):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='comments',
                             on_delete=models.CASCADE)

    reference = models.ForeignKey('self',
                            on_delete=models.CASCADE, blank=True, null=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_pk = models.SlugField()
    content_object = GenericForeignKey('content_type', 'object_pk')

    content = models.TextField()

    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    language = models.ForeignKey('Languege', on_delete=models.PROTECT, blank=True, null=True)

    # def __str__(self) -> str:
    #     return f"{self.content_type} {self.object_pk} user: {self.user}"

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_pk"]),
        ]


class TotalComments(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_pk = models.SlugField()
    content_object = GenericForeignKey('content_type', 'object_pk')

    total = models.PositiveBigIntegerField(default=0)

    # def __str__(self) -> str:
    #     return f"{self.content_type} {self.object_pk}-{self.total}"
    

class Languege(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(primary_key=True, unique=True)

    def __str__(self) -> str:
        return str(self.slug)


class Comments(models.Model):
    comments = GenericRelation(Comment, object_id_field='object_pk')
    total_comments = GenericRelation(TotalComments, object_id_field='object_pk')

    class Meta:
        abstract = True