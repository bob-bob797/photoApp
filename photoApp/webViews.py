import base64

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

def simple_upload(request):
    if request.method == 'POST':
        form = documentForm(request.POST, request.FILES)
        if form.is_valid():
            this_room = room.objects.filter(room_code=form.data["room_code"]).first()
            pic = base64.b64decode(form.data['picture'])
            with open(form.data['name']+'.jpg', 'wb+') as f:
                f.write(pic)
                pic = picture(name=form.data["name"] + '.jpg', room=this_room)
                pic.pic.save(form.data['name']+'.jpg', f)
                pic.save()
            return HttpResponse("Received")
