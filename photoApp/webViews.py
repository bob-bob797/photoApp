from django.http import HttpResponse
from rest_framework import generics
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

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


class displayPicture(generics.RetrieveAPIView):
    serializer_class = pictureSerializer
    queryset = picture.objects.all()

    def get_object(self):
        return picture.objects.all().first()


class PostPicture(generics.CreateAPIView):
    serializer_class = pictureSerializer

    def get_queryset(self):
        return room.objects.filter(room_code=self.kwargs["room_code"])

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')