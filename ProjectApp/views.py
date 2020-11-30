from django.shortcuts import render,redirect
from .models import Project,Profile
from django.contrib.auth.models import User
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import FormProject,FormProfile


# Create your views here.

def main(request):
        projects = Project.get_images()
        return render(request,"index.html",{"projects":projects})

# @login_required(login_url='/accounts/login/')
def project_new(request):
    current_user = request.user
    if request.method == 'POST':
        form = FormProject(request.POST,request.FILES)
        if form.is_valid():
            user_image = form.save()
            user_image.user = current_user
            user_image.save()

        return redirect('index')
    else:
        form = FormProject()
    return render(request,"project_now.html",{"form":form})


# @login_required(login_url='/accounts/login/')
def profile_new(request):
    current_user = request.user
    if request.method == 'POST':
        form = FormProfile(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user_profile = current_user
            profile.Id_profile = request.user.id
            profile.save()
        return redirect('profile')
    else:
        form = FormProfile()
    return render(request, 'profile_new.html', {"form": form})

# @login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    projects = Project.objects.filter(user = current_user)

    try:   
        profile = Profile.objects.get(user_profile=current_user)
    except ObjectDoesNotExist:
        return redirect('profilenew')

    return render(request,'profile/profile.html',{'profile':profile,'projects':projects})

def search_project(request):
    if 'project' in request.GET and request.GET ["project"]:
        search_term = request.GET.get("project")
        search_projects = Project.search_project_title(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {"message":message, "projects":search_project})

    else:
        message = "No search results yet!"
        return render (request, 'search.html', {"message": message})

