from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from files import services


class FileMixin:
    @action(methods=['POST'], detail=True)
    def create_file(self, request, pk=None):
        obj = self.get_object()
        request.data._mutable = True
        services.create_file(obj, request.data)
        return Response()

    @action(methods=['POST'], detail=True)
    def delete_file(self, request, pk=None):
        obj = self.get_object()
        request.data._mutable = True
        services.delete_file(obj, request.data)
        return Response()