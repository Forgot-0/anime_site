from django.contrib import admin
from .models import Reaction, UserReaction, TotalReaction
# Register your models here.
admin.site.register(Reaction)
admin.site.register(UserReaction)
admin.site.register(TotalReaction)