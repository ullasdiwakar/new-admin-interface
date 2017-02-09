from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from google.appengine.api import users
from google.appengine.ext import ndb
from models import Admins
from forms import LoginForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    url = users.create_login_url('user_auth/validate')
    return HttpResponseRedirect(url)

def logout(request):
    """Redirects to the homepage after logging the user out."""
    url = users.create_logout_url(reverse('home'))
    return HttpResponseRedirect(url)

def create_admin(request):
    ullas = Admins(email='ullasdiwakar96@gmail.com', fname='Ullas', lname='Diwakar', id='ullasdiwakar96@gmail.com')
    gaurang = Admins(email='gaurangrk@gmail.com', fname='Gaurang', lname='Kanvinde', id='gaurangrk@gmail.com')
    entity_list = [ullas, gaurang]
    list_of_keys = ndb.put_multi(entity_list)
    return HttpResponse("The Admins you wanted are created")

def validate(request):
    user = users.GetCurrentUser()
    email = user.email()
    admin_key = ndb.Key('Admins', email)
    admin = admin_key.get()
    if admin is None:
        msg = "Sorry, You are not an admin"
        return render(request, 'login_error.html', {'message' : msg})
    else:
        return HttpResponseRedirect('/home')