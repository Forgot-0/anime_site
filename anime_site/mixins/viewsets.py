from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.core.cache import cache

class RetrieveModelMixin:
    def retrieve(self, request, *args, **kwargs):
        instance = self.filter_queryset(self.get_queryset()).filter(pk=kwargs['pk'])
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data[0])


class CustomModelViewSet(RetrieveModelMixin, ModelViewSet):
    

    def list(self, request, *args, **kwargs):
        cache_key = f'{self.basename}_{self.action}'
        
        data = cache.get(cache_key)
        if data:
            return Response(data)
        
        response = super().list(request, *args, **kwargs)

        cache.set(cache_key, response.data, timeout=60*3) 
        return response
    
    def retrieve(self, request, *args, **kwargs):
        cache_key = f'{self.basename}_{self.kwargs["pk"]}'
        data = cache.get(cache_key)
        if data:
            return Response(data)
        
        response = super().retrieve(request, *args, **kwargs)

        cache.set(cache_key, response.data, timeout=60) 
        return response
    
    def create(self, request, *args, **kwargs):
        cache.delete(f'{self.basename}_list')
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        cache.delete(f'{self.basename}_{self.kwargs["pk"]}')
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        cache.delete(f'{self.basename}_{self.kwargs["pk"]}')
        return super().partial_update(request, *args, **kwargs)