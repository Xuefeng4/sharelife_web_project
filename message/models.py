from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from shareLife.models import  Post

DEFAULT_LOCATION_ID = 1
DEFAULT_POST_ID =1
DEFAULT_USER_ID =1

# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(User, related_name='send_chats', on_delete=models.CASCADE,default=DEFAULT_POST_ID)
    receiver = models.ForeignKey(User, related_name='recv_chats', on_delete=models.CASCADE,default=DEFAULT_POST_ID)
    content =  models.TextField(max_length=140,default="Hello from the other side")
    time = models.DateTimeField(auto_now_add=True, null=True)
    post = models.ForeignKey(Post, related_name="Message_post", on_delete= models.CASCADE,default=DEFAULT_POST_ID)

    def __unicode__(self):
        return u'%s' % self.content

    def get_absolute_url(self):
        return reverse('shareLife:chatPost', kwargs={'pk': self.postId})