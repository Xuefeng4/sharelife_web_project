# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import  reverse

import datetime


DEFAULT_LOCATION_ID = 1
DEFAULT_POST_ID =1
DEFAULT_USER_ID =1

class Category(models.Model):
    name = models.CharField(max_length=100)


class Tag(models.Model):
    name = models.CharField(max_length=100)



class Location(models.Model):
    name = models.CharField(max_length=100,default="Chicago")

    def __str__(self):
        return '%s' % self.name


class Post(models.Model):

    name = models.CharField(max_length=70)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField(max_length=500)

    created_time = models.DateField(default=datetime.date.today)
    modified_time = models.DateField(default=datetime.date.today)

    sqft = models.DecimalField(max_digits=6, decimal_places=2,blank = True, default =100)
    location = models.ForeignKey(Location,on_delete=models.CASCADE,default=DEFAULT_LOCATION_ID)
    tags = models.ManyToManyField(Tag, blank=True)
    address = models.CharField(max_length=200, blank=True)
    startDate = models.DateField(default=datetime.date.today)
    endDate = models.DateField(default=datetime.date.today)
    latitude = models.CharField(max_length=70, blank=True)
    longitude = models.CharField(max_length=70, blank=True)
    pic_url= models.URLField(max_length=200, blank=True)
    bedrooms = models.CharField(max_length=200, blank=True)
    bathrooms = models.CharField(max_length=200, blank=True)

    excerpt = models.TextField(max_length=500, blank=True)
    space_text = models.TextField(max_length=500, blank= True)
    transit_text = models.TextField(max_length=500, blank= True)
    access_text = models.TextField(max_length=500, blank= True)
    interaction_text = models.TextField(max_length=500, blank= True)
    amentity_text = models.TextField(max_length= 500, blank = True)


    def __str__(self):
        return self.name[:-5]

    def get_absolute_url(self):
        return reverse('shareLife:post_detail', kwargs={'pk': self.pk})
    def get_amenity(self):
        ret = []
        for str in self.amentity_text[1:-1].split(","):
            if str[0] == '"':
                str = str[1:-1]
            if not str.startswith("translation"):
                ret.append(str)
        return ret


# <<<<<<< HEAD
#
# class PostDetail(models.Model):
#     property_id = models.AutoField(primary_key= True)
#     description = models.CharField(max_length=200, blank=True)
#     name = models.ForeignKey(Post,on_delete=models.CASCADE,default=DEFAULT_LOCATION_ID)
#     location = models.ForeignKey(Location, on_delete=models.CASCADE, default=DEFAULT_LOCATION_ID)
# =======

class PostDetail(models.Model):
    description = models.CharField(max_length=200, blank=True)
    name = models.ForeignKey(Post,on_delete=models.CASCADE,default=DEFAULT_LOCATION_ID)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=DEFAULT_LOCATION_ID)





    # def __str__(self):
    #     return '%s' % self.property_size,\
               # '%s' % self.property_size,\
               # '%s' % self.bedrooms,\
               # '%s' % self.bathrooms, \
               # '%s' % self.garage_size, \
               # '%s' % self.year_built, \
               # '%s' % self.address, \
               # '%s' % self.price, \
               # '%s' % self.description, \
               # '%s' % self.name,

    # class Meta:
    #     ordering = ['property_size']




# class Message(models.Model):
#     text = models.CharField(max_length=140)
#
#     sender = models.ForeignKey(User, on_delete = models.CASCADE)
#     receiver  = models.ForeignKey(User, on_delete = models.CASCADE)
#     time = models.DateTimeField()
# class Message(models.Model):
#     text = models.CharField(max_length=140)
#
#     sender = models.ForeignKey(User, on_delete = models.CASCADE)
#     receiver  = models.ForeignKey(User, on_delete = models.CASCADE)
#     time = models.DateTimeField()


