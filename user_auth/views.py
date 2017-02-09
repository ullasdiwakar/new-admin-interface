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
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            admin_key = ndb.Key('Admins', email)
            admin = admin_key.get()
            if admin is None:
                msg = "Looks like you are not one of the admins."
                return render(request, 'login_error.html', {'message' : msg})
            else:
                url = users.create_login_url(dest_url=request.GET.get('next'))
                return HttpResponseRedirect(url)
    form = LoginForm()
    return render(request, 'login.html', {'form' : form})

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


"""
if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            admin_key = ndb.key('Admins', email)
            admin = admin_key.get()
            if admin is None:
                msg = "Looks like you are not one of the admins."
                return render(request, 'login_error.html', {'message' : msg})
            else:
                url = users.create_login_url(dest_url=request.GET.get('next'))
                return HttpResponseRedirect(url)
    form = LoginForm()
    return render(request, 'login.html', {'form' : form})
"""