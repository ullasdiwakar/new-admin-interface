from django import forms

class CreateForm(forms.Form):
    Id = forms.CharField(max_length=10, label="ID")
    name = forms.CharField(max_length=50, label="Name")
    lat = forms.CharField(max_length=15, label="Latitude")
    lng = forms.CharField(max_length=15, label="Longitude")
    level1 = forms.CharField(max_length=50, label="Level 1")
    level2 = forms.CharField(max_length=50, label="Level 2")
    level3 = forms.CharField(max_length=50, label="Level 3")
    status = forms.BooleanField()