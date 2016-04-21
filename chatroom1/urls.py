from django.conf.urls import patterns, url
from django.contrib import admin
from .views import *

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^chatroom/login$', log_in),
    url(r'^chatroom/$', chat_room),
    url(r'^chatroom/update$', update_messages),
    url(r'^index/$', Index.as_view()),
    url(r'^listMessages/$', MessagesList.as_view()),
    url(r'^chatroom/class-based-view$', Chat_room_class_based.as_view()),
)
