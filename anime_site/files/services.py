import os
from django.contrib.contenttypes.models import ContentType
from .models import Video, VoiceActing, Audio, Picture


file_types = {
    'video': Video,
    'audio': Audio,
    'img': Picture,
}

def file_generator(file_name, offset=0, length=None, chunk_size=8192):
    with open(file_name, "rb") as f:
        f.seek(offset)

        consumed = 0

        while True:
            data_length = min(chunk_size, length - offset - consumed) if length else chunk_size
            if data_length <= 0:
                break
            data = f.read(data_length)
            if not data:
                break
            consumed += data_length
            yield data
    

def get_file_response(request, path):
    lenght = os.path.getsize(path)
    status_code = 200
    content_range = request.headers.get('range')

    if content_range is not None:
        content_ranges = content_range.strip().lower().split('=')[-1]
        range_start, range_end, _ = map(str.strip, (content_ranges + '-').split('-'))
        range_start = max(0, int(range_start)) if range_start else 0
        range_end = min(lenght - 1, int(range_end)) if range_end else lenght - 1
        content_length = (range_end - range_start) + 1
        file = file_generator(path, range_start, range_end + 1)
        status_code = 206
        content_range = f'bytes {range_start}-{range_end}/{lenght}'

    return file, status_code, content_length, content_range

def create_file(obj, data):
    content_type = ContentType.objects.get_for_model(obj)
    file_model = file_types[data.pop("file_type")[0]]
    file_model.objects.create(object_pk=obj.pk, content_type=content_type, **data.dict())

def delete_file(obj, data):
    content_type = ContentType.objects.get_for_model(obj)
    file_model = file_types[data.pop("file_type")[0]]
    file_model.objects.filter(object_pk=obj.pk, content_type=content_type, **data.dict()).delete()
