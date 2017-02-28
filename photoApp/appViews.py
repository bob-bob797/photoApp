from django.http import HttpResponse
from rest_framework import generics

from .models import user, room, picture
from .serializer import roomSerializer


def photoOfTheDay(request):
    return HttpResponse(open("Dog.jpg", "rb").read(), content_type="image/jpg")