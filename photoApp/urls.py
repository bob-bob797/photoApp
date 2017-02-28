from django.conf.urls import url

from . import webViews
from . import appViews

urlpatterns = [
    #Web endpoints
    url(r'^$', webViews.index, name='index'),
    url(r'^room/createRoom/(?P<room_name>.+)/$', webViews.CreateRoom.as_view(), name='create_room'),
    url(r'^room/displayroom/(?P<room_code>.+)/$', webViews.DisplayRoom.as_view(), name='display_room'),

    url(r'^picture/postPicture/(?P<room_code>.+)/$', webViews.PostPicture.as_view(), name='post_picture'),


    #App endpoints
    url(r'^app$', appViews.photoOfTheDay, name='index'),
]