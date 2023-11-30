from rest_framework.fields import empty
from comments.models import Comment
from rest_framework import serializers
from reactions.api.mixins import ReactionMixinSerializer


class ComentSerializer(ReactionMixinSerializer, serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
            'pk',
            'user',
            'reference',
            'content',
            'date_create',
            'date_update',
            'is_react'
        )
    
    
