from django.contrib import admin
from .models import Anime, Season, Tag, Episode
# Register your models here.
admin.site.register(Anime)
admin.site.register(Season)
admin.site.register(Tag)
admin.site.register(Episode)