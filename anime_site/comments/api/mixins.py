from rest_framework.decorators import action
from rest_framework.response import Response
from comments import services
from .serializers import ComentSerializer


class CommentMixin:
    @action(methods=['POST'], detail=True)
    def ccomment(self, request, pk=None):
        obj = self.get_object() 
        services.create_comment(obj, request.user, request.data.get('content', ''), request.data.get('reference', None))
        return Response()

    @action(methods=['POST'], detail=True)
    def dcomment(self, request, pk=None):
        obj = self.get_object() 
        services.delete_comment(request.data['pk'])
        return Response()

    @action(methods=['GET'], detail=True)
    def comments(self, request, pk=None):
        obj = self.get_object()
        data = services.comments(obj)
        serializer = ComentSerializer(data, many=True, context={
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        })
        return Response(serializer.data)
