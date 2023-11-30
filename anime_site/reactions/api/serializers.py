from reactions.models import UserReaction, TotalReaction
from rest_framework import serializers



class ReactionsSerializer(serializers.ModelSerializer):
    reaction = serializers.SlugRelatedField(slug_field='slug', read_only=True)
    class Meta:
        model = UserReaction
        fields = ('reaction',)


class ReactionsSerializerList(serializers.RelatedField):
    def to_representation(self, value):
        return value.reaction.slug

class UserReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReaction
        fields = (
            'user',
            'reaction',
        )


class TotalReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalReaction
        fields = (
            'name',
            'total',
        )