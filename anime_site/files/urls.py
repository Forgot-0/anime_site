from django.urls import path
from .views import get_streaming_file


urlpatterns = [
    path('stream/<str:type>/<int:pk>/', get_streaming_file, name='stream'),
]
