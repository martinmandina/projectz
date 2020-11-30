from django import forms
from .models import Project,Profile

class FormProject(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','date']