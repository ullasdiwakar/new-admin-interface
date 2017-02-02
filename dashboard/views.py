from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from models import Installation
import csv
from google.appengine.ext import ndb
from forms import CreateForm, DeleteForm, EditForm, UpdateForm


@login_required(login_url = "user_auth/login/")
def home(request):
    create_form = CreateForm()
    edit_form = EditForm()
    delete_form = DeleteForm()
    return render(request, 'home.html', {'create_form' : create_form, 'edit_form' : edit_form, 'delete_form' : delete_form})

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
    msg = "Oops, Looks like the data you entered was improper!!"
    return render(request, 'error.html', {'message' : msg})

def delete(request):
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            Id = int(form.cleaned_data['Id'])
            if form.cleaned_data['Id'] is None:
                msg = "Oops, Looks like the data you entered was improper!!"
                return render(request, 'error.html', {'message' : msg})
            tower_key = ndb.Key(Installation, Id)
            tower = tower_key.get()
            if tower is None:
                msg = "Sorry, An Entity with that ID does not exist on the Datastore!!"
                return render(request, 'error.html', {'message' : msg})
            tower_key.delete()
            msg = "Entity Deleted Successfully"
            return render(request, 'success.html', {'message' : msg})
    msg = "Oops, Looks like the data you entered was improper!!"
    return render(request, 'error.html', {'message' : msg})

def edit_screen(request):
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            Id = int(form.cleaned_data['Id'])
            if form.cleaned_data['Id'] is None:
                msg = "Oops, Looks like the data you entered was improper!!"
                return render(request, 'error.html', {'message' : msg})
            tower_key = ndb.Key(Installation, Id)
            tower = tower_key.get()
            if tower is None:
                msg = "Sorry, An Entity with that ID does not exist on the Datastore!!"
                return render(request, 'error.html', {'message' : msg})
            entity_properties = dict()
            entity_properties['Id'] = tower.Id
            entity_properties['name'] = tower.name
            entity_properties['lat'] = tower.lat
            entity_properties['lng'] = tower.lng
            entity_properties['Level-1'] = tower.level1
            entity_properties['Level-2'] = tower.level2
            entity_properties['Level-3'] = tower.level3
            entity_properties['status'] = tower.status
            update_form = UpdateForm()
            return render(request, 'update.html', {'details' : entity_properties, 'update_form' : update_form})
    msg = "Oops, Looks like the data you entered was improper!!"
    return render(request, 'error.html', {'message' : msg}) 

def update(request):
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            Id = int(form.cleaned_data['Id'])
            tower_key = ndb.Key(Installation, Id)
            tower = tower_key.get()
            if tower is None:
                msg = "Please enter the correct ID."
                return render(request, 'error.html', {'message' : msg})
            if form.cleaned_data['name'] != '':
                tower.name = form.cleaned_data['name']
            if form.cleaned_data['lat'] != '':
                tower.lat = float(form.cleaned_data['lat'])
            if form.cleaned_data['lng'] != '':
                tower.lng = float(form.cleaned_data['lng'])
            if form.cleaned_data['level1'] != '':
                tower.level1 = form.cleaned_data['level1']
            if form.cleaned_data['level2'] != '':
                tower.level2 = form.cleaned_data['level2']
            if form.cleaned_data['level3'] != '':
                tower.level3 = form.cleaned_data['level3']
            if form.cleaned_data['status'] is not None:
                tower.status = form.cleaned_data['status']
            new_key = tower.put()
            msg = "Entity Updated Successfully"
            return render(request, 'success.html', {'message' : msg})
    msg = "Oops, Looks like the data you entered was improper!!"
    return render(request, 'error.html', {'message' : msg})