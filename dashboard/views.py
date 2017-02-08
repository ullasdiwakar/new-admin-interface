from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from models import Installation
import csv
import json
from django.views.decorators.csrf import csrf_exempt
from google.appengine.ext import ndb
from forms import CreateForm, DeleteForm, EditForm, UpdateForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


#@login_required(login_url = "user_auth/login/")
def home(request):
    create_form = CreateForm()
    edit_form = EditForm()
    delete_form = DeleteForm()
    query = "SELECT * FROM Installation"
    towers_list = ndb.gql(query).fetch()
    paginator = Paginator(towers_list, 10)
    page = request.GET.get('page')
    try:
        towers = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        towers = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        towers = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'create_form' : create_form, 'edit_form' : edit_form, 'delete_form' : delete_form, 'towers' : towers})

def create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            Id = form.cleaned_data['Id']
            tower_key = ndb.Key(Installation, int(Id))
            tower = tower_key.get()
            if tower is None:
                pass
            else:
                data = form.cleaned_data
                create_form = CreateForm(initial=data)
                return render(request, 'confirm.html', {'data' : data, 'create_form' : create_form})
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
            entity_properties['level1'] = tower.level1
            entity_properties['level2'] = tower.level2
            entity_properties['level3'] = tower.level3
            entity_properties['status'] = tower.status
            update_form = UpdateForm(initial=entity_properties)
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

def overwrite(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if 'cancel' in request.POST:
            return HttpResponseRedirect('/home')
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
            msg = "Entity Overwritten Successfully"
            return render(request, 'success.html', {'message' : msg})
    msg = "Oops, Looks like the data you entered was improper!!"
    return render(request, 'error.html', {'message' : msg})

@csrf_exempt
def delete_entities(request):
    items = request.POST.getlist('IDs[]')
    id_str = ''
    for i in items:
        id_str = id_str + i + ', '
        tower_key = ndb.Key(Installation, int(i))
        tower = tower_key.get()
        if tower is None:
            data = {'message': 'Sorry, does not exist'}
            return JsonResponse(data)
        tower.key.delete()
    data = {'message': 'Deleted Entities with IDs %s.'%id_str[:-2]}
    return JsonResponse(data)

def createentity(request):
    mum1 = Installation(Id=1,	name='Mum1',	lat=18.9913345,	lng=72.811139,	level1='Maharashta',	level2='MahWest',	level3='Mumbai',	status=False, id=1)
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

    entity_list = [mum1, mum2, mum3, pune1, pune2, pune3, ngp1, ngp2, ngp3, blr1, blr2, blr3]
    list_of_keys = ndb.put_multi(entity_list)
    return HttpResponse("The entities you wanted are Entities created")