from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

class RetrieveModelMixin:
    def retrieve(self, request, *args, **kwargs):
        instance = self.filter_queryset(self.get_queryset()).filter(pk=kwargs['pk'])
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data[0])


class CustomModelViewSet(RetrieveModelMixin, ModelViewSet):
    pass