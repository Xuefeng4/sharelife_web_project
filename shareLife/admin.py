from django.contrib import admin
from .models import  Post

from shareLife.models import Category, Tag, Location, Post, PostDetail

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Location)
admin.site.register(Post)

admin.site.register(PostDetail)

