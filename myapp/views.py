from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import AddForm
# Create your views here.

people = []

class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return self.username


def index(request):
    return render(request, 'index.html',{'people':people})

def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            person = Person(username=username, password=password)
            people.append(person)
            return HttpResponseRedirect('/')
    else:
        form = AddForm()
        return render(request, 'add.html', {'form': form, 'people': people})