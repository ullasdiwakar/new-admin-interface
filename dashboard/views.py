from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from models import Installation
import csv
from google.appengine.ext import ndb
from forms import CreateForm


@login_required(login_url = "user_auth/login/")
def home(request):
    form = CreateForm()
    return render(request, 'home.html', {'form' : form})

def create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            Id = form.cleaned_data['Id']
            name = form.cleaned_data['name']
            lat = float(form.cleaned_data['lat'])
            lng = float(form.cleaned_data['lng'])
            level1 = form.cleaned_data['level1']
            level2 = form.cleaned_data['level2']
            level3 = form.cleaned_data['level3']
            status = form.cleaned_data['status']
            new_tower = Installation(Id=int(Id), name=name, lat=lat, lng=lng, level1=level1, level2=level2, level3=level3, status=status, id=int(Id))
            tower_key = new_tower.put()
            msg = "Entity Created Successfully"
            return render(request, 'success.html', {'message' : msg})
    return render(request, 'error.html')