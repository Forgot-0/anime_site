from rest_framework import serializers
from persons.models import Person
from reactions.api.mixins import ReactionMixinSerializer
from files.api.serializers import PictureListDetailSerializer, AudioDetailSerializer
from animes.models import Anime

class PersonSerializer(ReactionMixinSerializer, serializers.ModelSerializer):
    imgs = PictureListDetailSerializer(many=True, read_only=True)
    anime_pk = serializers.PrimaryKeyRelatedField(queryset=Anime.objects.all(), source='anime', write_only=True)

    class Meta:
        model = Person
        fields = (
            'title',
            'slug',
            'avatar',
            'description',
            'imgs',
            'is_react',
            'anime',
            'anime_pk',    
            )
        depth = 1


class PersonDetailSerializer(ReactionMixinSerializer, serializers.ModelSerializer):
    imgs = PictureListDetailSerializer(many=True, read_only=True)
    persons = serializers.SerializerMethodField()
    voices = AudioDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Person
        fields = (
            'title',
            'slug',
            'avatar',
            'description',
            'imgs',
            'voices',
            'is_react',
            'persons',
            'anime',
            'persons',
            )
        depth = 1

    def get_persons(self, obj):
        return Person.objects.all().exclude(pk=obj.pk).values('title', 'slug', 'avatar')