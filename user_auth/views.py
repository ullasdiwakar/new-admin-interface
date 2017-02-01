from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from google.appengine.api import users


def login(request):
    """Redirects to the Google App Engine authentication page."""
    url = users.create_login_url(dest_url=request.GET.get('next'))
    return HttpResponseRedirect(url)

def logout(requesr):
    """Redirects to the homepage after logging the user out."""
    url = users.create_logout_url(reverse('home'))
    return HttpResponseRedirect(url)
