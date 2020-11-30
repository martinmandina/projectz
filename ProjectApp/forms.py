from django import forms
from .models import Project,Profile

class FormProject(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','date']

class FormProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user_profile','Id_profile']
