from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image

def index(request):
    return HttpResponse(open("Dog.jpg").read())

def appIndex(request):
    return open("Dog.jpg").read()
