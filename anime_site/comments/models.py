from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
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

    # language = models.CharField(max_length=6, blank=True)

    def __str__(self) -> str:
        return f"{self.content_type} {self.object_pk} user: {self.user}"



class TotalComments(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_pk = models.SlugField()
    content_object = GenericForeignKey('content_type', 'object_pk')

    total = models.PositiveBigIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.content_type} {self.object_pk}-{self.total}"