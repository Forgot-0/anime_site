from django.contrib import admin
from .models import Comment, TotalComments, Languege

# Register your models here.
admin.site.register(Comment)
admin.site.register(Languege)
admin.site.register(TotalComments)