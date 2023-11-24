from rest_framework import serializers
from files.models import VoiceActing, Video, Picture, Audio



class VoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceActing
        fields = ('name', )


class VideoListDetailSerializer(serializers.ModelSerializer):
    voice = VoiceSerializer(read_only=True)
    url = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = ('res', 'voice', 'url')

    def get_url(self, obj):
        return f'/files/stream/video/{obj.pk}/'


class PictureListDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('img')


class AudioDetailSerializer(serializers.ModelSerializer):
    voice = VoiceSerializer(read_only=True)
    url = serializers.SerializerMethodField()
    
    class Meta:
        model = Audio
        fields = ('voice', 'url')

    def get_url(self, obj):
        return f'/files/stream/audio/{obj.pk}/'