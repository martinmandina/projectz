from django.shortcuts import render,redirect
from .models import Project,Profile
from django.contrib.auth.models import User
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def main(request):
    projects = Project.objects.all()
    return render(request, 'index.html',{'projects':projects})



