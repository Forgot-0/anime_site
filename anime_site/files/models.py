from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType, ContentTypeManager


# class MyFileModel(models.Model):
#     file_field_name = models.FileField(...)

#     def delete(self, *args, **kwargs):
#         # До удаления записи получаем необходимую информацию
#         storage, path = self.file_field_name.storage, self.file_field_name.path
#         # Удаляем сначала модель ( объект )
#         super(MyFileModel, self).delete(*args, **kwargs)
#         # Потом удаляем сам файл
#         storage.delete(path)


# Create your models here.
def video_path(instance, filename):
    return f'video/{instance.object_pk}/{filename}'


class Video(models.Model):

    CHOICE = (
        ('1080p', '1080p'),
        ('720', '720'),
        ('480', '480'),
    )

    res = models.CharField(max_length=5, choices=CHOICE)
    content = models.FileField(upload_to=video_path, validators=[FileExtensionValidator(allowed_extensions=['mp4'])])

    voice = models.ForeignKey('VoiceActing', on_delete=models.CASCADE, blank=True, null=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_pk = models.SlugField()
    content_object = GenericForeignKey('content_type', 'object_pk')

    def __str__(self) -> str:
        return f'{self.content_type}-{self.res}'
    
    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_pk"]),
        ]


class Audio(models.Model):
    content = models.FileField(upload_to='') 
    voice = models.ForeignKey('VoiceActing', on_delete=models.CASCADE, blank=True, null=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_pk = models.SlugField()
    content_object = GenericForeignKey('content_type', 'object_pk')

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_pk"]),
        ]


class VoiceActing(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.name}'


class Picture(models.Model):
    img = models.ImageField(upload_to='pictures/')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_pk = models.SlugField()
    content_object = GenericForeignKey('content_type', 'object_pk')

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_pk"]),
        ]