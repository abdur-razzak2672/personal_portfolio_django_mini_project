from django.shortcuts import render
from .models import project

def home(request) :
    projects = project.objects.all()
    return render(request , 'portfolio/home.html', {'projects':projects})
