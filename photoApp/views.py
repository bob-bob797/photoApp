from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image

def index(request):
    return HttpResponse("Welcome to the app backend")

def photoOfTheDay(request):
    return HttpResponse(open("Dog.jpg", "rb").read(), content_type="image/jpg")
