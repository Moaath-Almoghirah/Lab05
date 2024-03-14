from django import forms

class AddForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password')