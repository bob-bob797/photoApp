from django.http import HttpResponse
from rest_framework import generics

from .models import user, room, picture
from .serializer import roomSerializer, pictureSerializer
from .forms import documentForm


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

def postPicture(request):
    if request.method == ' POST':
        print request.FILES['file']
    return HttpResponse("Thanks")

class PostPicture(generics.CreateAPIView):
    serializer_class = pictureSerializer

    def get_queryset(self):
        return room.objects.filter(room_code=self.kwargs["room_code"])

@
def simple_upload(request):
    if request.method == 'POST':
        form = documentForm(request.POST, request.FILES)
        if form.is_valid():
            this_room = room.objects.filter(room_code=form.data["room_code"]).first()
            pic = picture(pic=request.FILES['picture'], name=form.data["name"], room=this_room)
            pic.save()
            return HttpResponse("Received")