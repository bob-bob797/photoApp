from django.conf.urls import url

from . import webViews

urlpatterns = [
    url(r'^$', webViews.index, name='index'),
    url(r'^room/createRoom/(?P<room_name>.+)/$', webViews.CreateRoom.as_view(), name='create_room'),
    url(r'^room/displayRoom/(?P<room_code>.+)/$', webViews.DisplayRoom.as_view(), name='display_room'),

    url(r'^upload/$', webViews.simple_upload, name='post_picture'),

]
