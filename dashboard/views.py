from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from models import Installation
import csv
from google.appengine.ext import ndb


@login_required(login_url = "user_auth/login/")
def home(request):
    return HttpResponse("You are at home Mr. Monkey D. Luffy")

def create(request):
    mum2 = Installation(Id=2,	name='Mum2',	lat=18.9913045,	lng=72.8221139,	level1='Maharashta',	level2='MahWest',	level3='Mumbai',	status=False, id=2)
    mum3 = Installation(Id=3,	name='Mum3',	lat=19.0450229,	lng=72.8837403,	level1='Maharashta',	level2='MahWest',	level3='Mumbai',	status=True, id=3)
    pune1 = Installation(Id=4,	name='Pune1',	lat=18.5166064,	lng=73.858734,	level1='Maharashta',	level2='MahWest',	level3='Pune',	status=False, id=4)
    pune2 = Installation(Id=5,	name='Pune2',	lat=18.5108685,	lng=73.857747,	level1='Maharashta',	level2='MahWest',	level3='Pune',	status=True, id=5)
    pune3 = Installation(Id=6,	name='Pune3',	lat=18.5287734,	lng=73.8664159,	level1='Maharashta',	level2='MahWest',	level3='Pune',	status=False, id=6)
    ngp1 = Installation(Id=7,	name='NGP1',	lat=21.1520351,	lng=79.0881544,	level1='Maharashta',	level2='MahEast',	level3='Nagpur',	status=True, id=7)
    ngp2 = Installation(Id=8,	name='NGP2',	lat=21.1543565,	lng=79.1031318,	level1='Maharashta',	level2='MahEast',	level3='Nagpur',	status=False, id=8)
    ngp3 = Installation(Id=9,	name='NGP3',	lat=21.1432696,	lng=79.0720182,	level1='Maharashta',	level2='MahEast',	level3='Nagpur',	status=True, id=9)
    blr1 = Installation(Id=10,	name='BLR1',	lat=12.9619269,	lng=77.646056,	level1='Karnataka',	level2='KarSouth',	level3='Bangalore',	status=False, id=10)
    blr2 = Installation(Id=11,	name='BLR2',	lat=12.9636416,	lng=77.6153287,	level1='Karnataka',	level2='KarSouth',	level3='Bangalore',	status=True, id=11)
    blr3 = Installation(Id=12,	name='BLR3',	lat=12.9485436,	lng=77.6037415,	level1='Karnataka',	level2='KarSouth',	level3='Bangalore',	status=False, id=12)

    entity_list = [mum2, mum3, pune1, pune2, pune3, ngp1, ngp2, ngp3, blr1, blr2, blr3]
    list_of_keys = ndb.put_multi(entity_list)
    return HttpResponse("The entities you wanted are Entities created")
