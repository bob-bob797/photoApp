from rest_framework import serializers
from django.core import serializers as coreSer
from django.conf import settings

from .models import user, room, picture


class roomSerializer(serializers.ModelSerializer):
    def get_pictures(self, obj):
        host = self.context['request']._request.META['HTTP_HOST']
        pics = []
        for pic in picture.objects.all().filter(room__room_code=obj.room_code):
            pics.append(
                {
                    'URL': "http://" + host + pic.pic.url,
                    'Name': pic.name,
                    'Created': pic.created_at
                }
            )
        return pics

    pictures = serializers.SerializerMethodField()

    class Meta:
        model = room
        fields = ('name', 'room_code', 'pictures')


class pictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = picture
        fields = ('name', 'created_at', 'pic',)
