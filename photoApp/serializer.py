from rest_framework import serializers
import base64

from .models import user, room, picture


class roomSerializer(serializers.ModelSerializer):
    def get_pictures(self, obj):
        pics = []
        for pic in picture.objects.all().filter(room__room_code=obj.room_code):
            pics.append({"name": pic.name, "created": pic.created_at, "data": base64.b64encode(pic.pic.read())})
        return pics

    pictures = serializers.SerializerMethodField()

    class Meta:
        model = room
        fields = ('name', 'room_code', 'pictures')


class pictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = picture
        fields = ('name', 'created_at', 'pic',)
