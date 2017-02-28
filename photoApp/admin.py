from django.contrib import admin

from .models import room, picture, user

admin.site.register(room)
admin.site.register(picture)
admin.site.register(user)
