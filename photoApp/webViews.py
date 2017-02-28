from django.http import HttpResponse
from rest_framework import generics

from .models import user, room, picture
from .serializer import roomSerializer, pictureSerializer


def index(request):
    return HttpResponse("Welcome to the app backend")


class CreateRoom(generics.CreateAPIView):
    serializer_class = roomSerializer
    queryset = room.objects.all()


class DisplayRoom(generics.ListAPIView):
    serializer_class = roomSerializer

    def get_queryset(self):
        return room.objects.filter(room_code=self.kwargs["room_code"])


class PostPicture(generics.CreateAPIView):
    serializer_class = pictureSerializer

    def get_queryset(self):
        return room.objects.filter(room_code=self.kwargs["room_code"])

