from django import forms
from choices import *

class CreateForm(forms.Form):
    Id = forms.CharField(max_length=10, label="ID")
    name = forms.CharField(max_length=50, label="Name")
    lat = forms.CharField(max_length=15, label="Latitude")
    lng = forms.CharField(max_length=15, label="Longitude")
    level1 = forms.CharField(max_length=50, label="Level 1")
    level2 = forms.CharField(max_length=50, label="Level 2")
    level3 = forms.CharField(max_length=50, label="Level 3")
    status = forms.ChoiceField(choices = STATUS_CHOICES, label="Status", initial='', widget=forms.Select(), required=True)

class DeleteForm(forms.Form):
    Id = forms.CharField(max_length=10, label="ID")

class EditForm(forms.Form):
    Id = forms.CharField(max_length=10, label="ID")

class UpdateForm(forms.Form):
    Id = forms.CharField(max_length=10, label="ID", required=False)
    name = forms.CharField(max_length=50, label="Name", required=False)
    lat = forms.CharField(max_length=15, label="Latitude", required=False)
    lng = forms.CharField(max_length=15, label="Longitude", required=False)
    level1 = forms.CharField(max_length=50, label="Level 1", required=False)
    level2 = forms.CharField(max_length=50, label="Level 2", required=False)
    level3 = forms.CharField(max_length=50, label="Level 3", required=False)
    status = forms.ChoiceField(choices = STATUS_CHOICES, label="Status", initial='', widget=forms.Select(), required=True)