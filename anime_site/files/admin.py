from django.contrib import admin
from .models import Video, VoiceActing, Audio, Picture

# Register your models here.
admin.site.register(Video)
admin.site.register(VoiceActing)
admin.site.register(Audio)
admin.site.register(Picture)
