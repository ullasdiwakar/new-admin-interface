from __future__ import unicode_literals
from google.appengine.ext import ndb
from django.db import models

class Installation(ndb.Model):
    Id = ndb.IntegerProperty()
    name = ndb.StringProperty()
    lat = ndb.FloatProperty()
    lng = ndb.FloatProperty()
    level1 = ndb.StringProperty()
    level2 = ndb.StringProperty()
    level3 = ndb.StringProperty()
    status = ndb.BooleanProperty()
