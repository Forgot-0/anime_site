from rest_framework import viewsets
from persons.models import Person
from .serializers import PersonSerializer, PersonDetailSerializer
from rest_framework.response import Response
from files.api.mixins import FileMixin
from mixins.viewsets import CustomModelViewSet
    


class PersonViewSet(CustomModelViewSet):
    queryset = Person.objects.all().prefetch_related('anime__genres', 'anime__topics', 'anime__years', 'imgs').select_related('anime')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PersonDetailSerializer
        return PersonSerializer
