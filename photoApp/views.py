from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image

def index(request):
    return HttpResponse(Image.open("Dog.jpg"))

def appIndex(request):
    return Image.open("Dog.jpg")