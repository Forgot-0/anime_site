from rest_framework import viewsets
from persons.models import Person
from .serializers import PersonSerializer, PersonDetailSerializer
from rest_framework.response import Response
from files.api.mixins import FileMixin
from reactions.api.mixins import ReactionMixin
from mixins.viewsets import CustomModelViewSet
from django_filters.rest_framework import DjangoFilterBackend


class PersonViewSet(CustomModelViewSet, ReactionMixin):
    queryset = Person.objects.prefetch_related('anime__genres', 'anime__topics', 'anime__years', 'imgs').select_related('anime').all()
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ('anime', )


    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PersonDetailSerializer
        return PersonSerializer
