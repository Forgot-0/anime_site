from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from reactions import services
from .serializers import UserReactionSerializer, TotalReactionSerializer



class ReactiondMixin:
    @action(methods=['POST'], detail=True)
    def reaction(self, request, pk=None):
        obj = self.get_object()
        services.add_reaction(obj, request.user, request.data.get('reaction', ''))
        return Response()

    @action(methods=['POST'], detail=True)
    def unreaction(self, request, pk=None):
        obj = self.get_object()
        services.remove_reaction(obj, request.user, request.data.get('reaction', ''))
        return Response()

    @action(methods=['GET'], detail=True)
    def reacs(self, request, pk=None):
        obj = self.get_object()
        reacs = services.get_react(obj)
        serializer = UserReactionSerializer(reacs, many=True)
        return Response(serializer.data)
    
    @action(methods=['GET'], detail=True)
    def total_reacs(self, request, pk=None):
        obj = self.get_object()
        totals = services.total_react(obj)
        serializer = TotalReactionSerializer(totals, many=True)
        return Response(serializer.data)
    
    @action(methods=['GET'], detail=False)
    def get_favs(self, request):
        queryset = (self.queryset.filter(reactions__reaction__slug=request.data.get('reaction', 'like'), reactions__user=request.user))
        data = self.get_serializer_class()(queryset, many=True, context={
            'request': self.request,
            'format': self.format_kwarg,
            'view': self,
        }).data
        return Response(data)


class ReactionMixinSerializer(serializers.Serializer):
    is_react = serializers.SerializerMethodField()
    total_react = serializers.SerializerMethodField()

    def get_is_react(self, obj):
        user = self.context.get('request').user
        return services.is_react(obj, user)
    
    def get_total_react(self, obj):
        return services.total_react(obj).values('name', 'total')


class LikeDislikeMixinSerializer(serializers.Serializer):
    like = serializers.SerializerMethodField()
    dislike = serializers.SerializerMethodField()

    def get_like(self, obj):
        return services.total_react(obj, reaction_slug='like').values_list('total', flat=True)

    def get_dislike(self, obj):
        return services.total_react(obj, reaction_slug='dislike').values_list('total', flat=True)


class FavoriteMixinSerializer(serializers.Serializer):
    favorite = serializers.SerializerMethodField()

    def get_favorite(self, obj):
        return services.total_react(obj, reaction_slug='favorite').values('total')