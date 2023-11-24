from django.contrib.contenttypes.models import ContentType
from .models import Comment, TotalComments



def create_comment(obj, user, content,  reference=None):
    obj_type = ContentType.objects.get_for_model(obj)

    if reference:
        reference = Comment.objects.get(pk=reference)

    data = Comment.objects.create(
        content_type=obj_type, object_pk=obj.pk, user=user, reference=reference, content=content
    )

    if data:
        totalcom, is_created = TotalComments.objects.get_or_create(content_type=obj_type, object_pk=obj.pk)
        totalcom.total += 1
        totalcom.save(update_fields=['total'])

def delete_comment(pk):
    data = Comment.objects.filter(pk=pk).first()

    if data:
        totalcom, is_created = TotalComments.objects.get_or_create(content_type=data.content_type, object_pk=data.object_pk)
        totalcom.total -= 1
        totalcom.save(update_fields=['total'])
        data.delete()


def comments(obj):
    obj_type = ContentType.objects.get_for_model(obj)
    return Comment.objects.filter(content_type=obj_type, object_pk=obj.pk)