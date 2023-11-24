from django.contrib.contenttypes.models import ContentType
from django.db.models import F
from .models import UserReaction, TotalReaction, Reaction


def add_reaction(obj, user, reaction_slug) -> bool:
    obj_type = ContentType.objects.get_for_model(obj)
    reaction = Reaction.objects.get(pk=reaction_slug)
    data, is_created = UserReaction.objects.get_or_create(
        content_type=obj_type, object_pk=obj.pk, user=user, reaction=reaction)

    if is_created:
        record, is_created = TotalReaction.objects.get_or_create(content_type=obj_type, object_pk=obj.pk, name=reaction)
        record.total += 1
        record.save(update_fields=['total'])

def remove_reaction(obj, user, reaction_slug) -> bool:
    obj_type = ContentType.objects.get_for_model(obj)
    reaction = Reaction.objects.get(pk=reaction_slug)
    answer = UserReaction.objects.filter(
        content_type=obj_type, object_pk=obj.pk, user=user, reaction=reaction
    ).delete()

    if answer[0]:
        record, is_created = TotalReaction.objects.get_or_create(content_type=obj_type, object_pk=obj.pk, name=reaction)
        if not is_created:
            record.total -= 1
            record.save(update_fields=['total'])


def is_react(obj, user):
    if not user.is_authenticated:
        return False
    obj_type = ContentType.objects.get_for_model(obj)
    reactions = UserReaction.objects.filter(
        content_type=obj_type, object_pk=obj.pk, user=user)
    return reactions.values_list('reaction', flat=True)


def get_react(obj):
    obj_type = ContentType.objects.get_for_model(obj)
    return UserReaction.objects.filter(content_type=obj_type, object_pk=obj.pk)


def total_react(obj, reaction_slug=None):
    obj_type = ContentType.objects.get_for_model(obj)
    if reaction_slug:
        return TotalReaction.objects.filter(content_type=obj_type, object_pk=obj.pk, name_id=reaction_slug)
    return TotalReaction.objects.filter(content_type=obj_type, object_pk=obj.pk)
