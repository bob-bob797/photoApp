from __future__ import unicode_literals
from django.db import models

import uuid


def picture_path(instance, name):
    return 'pictures/{0}/{1}'.format(instance.room.room_code, name)

class room(models.Model):
    name = models.CharField(max_length=50)
    room_code = models.CharField(max_length=50, unique=True, default=uuid.uuid4)

    def __str__(self):
        return self.name

class picture(models.Model):
    name = models.CharField(max_length=100, null=True)
    room = models.ForeignKey(room)
    created_at = models.DateTimeField(auto_now_add=True)
    pic = models.ImageField(upload_to=picture_path)

    def __str__(self):
        return self.name

class user(models.Model):
    nickname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    rooms = models.ManyToManyField(room)

    def __str__(self):
        return self.nickname
