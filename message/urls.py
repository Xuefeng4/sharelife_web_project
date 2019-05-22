from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'message'
urlpatterns = [
    url(r'^message/'
        r'post/(?P<pk>[0-9]+)/$', views.detailPost, name='post_message'),
    url(r'^message/'
        r'post/(?P<post>[0-9]+)/(?P<user1>[0-9]+)/(?P<user2>[0-9]+)/$', views.chatRoom, name='chatRoom'),
    url(r'^message/'
        r'posted/(?P<post>[0-9]+)/(?P<user1>[0-9]+)/(?P<user2>[0-9]+)/$', views.chatPost, name='chat_message'),

]