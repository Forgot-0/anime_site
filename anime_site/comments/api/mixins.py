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
        services.delete_comment(request.data['pk'])
        return Response()

    @action(methods=['GET'], detail=True)
    def comments(self, request, pk=None):
        obj = self.get_object()
        language = (request.META['HTTP_ACCEPT_LANGUAGE'].split(',')[0])
        data = services.comments(obj, language)
        return self.get_list_comment(data)

    def get_commentserializer(self, data, many=False):
        serializer = ComentSerializer(data, many=many, context={
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        })
        return serializer

    def get_list_comment(self, queryset):
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_commentserializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        data = self.get_commentserializer(queryset, many=True).data

        return Response(data)
