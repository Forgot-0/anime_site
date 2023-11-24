from django.http import StreamingHttpResponse
from .services import get_file_response
from .models import Video, Audio

# Create your views here.

def get_streaming_file(request, type, pk):
    types = {
        'video': [Video, 'video/'],
        'audio': [Audio, 'audio/'],
    }

    path, type = types[type]
    path = path.objects.get(pk=pk)

    file, status_code, content_length, content_range = get_file_response(request, path.content.path)
    response = StreamingHttpResponse(file, status=status_code, content_type=f"{type}{path.content.name.split('.')[-1]}")

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response

