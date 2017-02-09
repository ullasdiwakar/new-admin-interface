from __future__ import unicode_literals
from google.appengine.ext import ndb
from django.db import models

class Admins(ndb.Model):
    email = ndb.StringProperty()
    fname = ndb.StringProperty()
    lname = ndb.StringProperty()
