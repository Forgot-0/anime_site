from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Anime


@registry.register_document
class AnimeDocument(Document):

    class Index:
        name = 'animes'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Anime
        fields = [
            'title',
            'slug',
            'description',
            'image',
         ]