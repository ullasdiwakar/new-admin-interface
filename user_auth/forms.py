from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(max_length=70, label="Email ID", widget=forms.EmailInput)