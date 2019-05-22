import csv

from django.contrib.auth.models import User

from shareLife.models import Post, Location
import time
import random

import datetime
import radar


city_dict = {"1":"chicago","2":"boston", "3":"nyc", "4":"la", "5":"sf", "6":"seattle","7":'austin'}
for key, value in city_dict.items():
    path = "./data/"+ value +".csv"
    with open(path, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        # j = 0
        # for row in data:
        #     if j >= 1:
        #         break
        #     j+= 1
        i = 0
        for row in data:
            if i > 100:
                break
            if i == 0:
                i += 1
            #user
            #print(row)
            else:
                name_ = row[21]
                print (name_)
                tail = str(random.randint(1, 100000))
                user = User.objects.create_user(username = name_+tail, password='123456')
                user.save()

                loc = Location.objects.get(pk = key)
                userid = User.objects.get(username = name_ + tail)

                # excerpt = models.TextField(max_length=500, blank=True)
                # space_text = models.TextField(max_length=500, blank=True)
                # transit_text = models.TextField(max_length=500, blank=True)
                # access_text = models.TextField(max_length=500, blank=True)
                # interaction_text = models.TextField(max_length=500, blank=True)
                # amentity_text = models.TextField(max_length=500, blank=True)

                # print(userid)
                # print("row58",row[59])
                if len(row[59].strip()) == 0:
                    row[59] = 0

                start = radar.random_datetime(start='2019-03-01', stop='2019-04-15')
                end = radar.random_datetime(start='2019-04-16', stop='2019-05-30')

                P = Post(name = row[4],body= row[5],excerpt = row[5],space_text = row[6],transit_text = row[11],access_text = row[12],
                         interaction_text = row[13], amentity_text= row[58], sqft= row[59],location = loc,author = userid, latitude=row[48] ,
                         longitude= row[49], pic_url=row[17], bedrooms = row[55], bathrooms = row[54],startDate = start, endDate = end)

                P.save()
                i += 1

