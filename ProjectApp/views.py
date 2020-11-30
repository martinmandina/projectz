from django.shortcuts import render,redirect
from .models import Project,Profile
from django.contrib.auth.models import User
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import FormProject


# Create your views here.

def main(request):
        projects = Project.get_images()
        return render(request,"index.html",{"projects":projects})

# @login_required(login_url='/accounts/login/')
def project_new(request):
    logged_user = request.user
    if request.method == 'POST':
        form = FormProject(request.POST,request.FILES)
        if form.is_valid():
            user_image = form.save()
            user_image.user = logged_user
            user_image.save()

        return redirect('index')
    else:
        form = FormProject()
    return render(request,"project_now.html",{"form":form})