from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    link = models.URLField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title

    def project_save(self):
        self.save()

    def project_delete(self):
        self.delete()

    def profile_update(self):
        self.save()

    @classmethod
    def search_project_title(cls,search_term):
        project = cls.objects.filter(title__icontains=search_term)
        return project

    @classmethod
    def get_images(cls):
        images_all = Project.objects.all()
        return images_all
    @classmethod
    def find_project(cls, project):
        project = cls.objects.get(id=project)
        return project

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='profilePics/', blank=True,null=True)
    bio = models.TextField()     
    contacts = models.CharField(max_length=20)
    user_profile = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    profile_Id = models.IntegerField(default=0)

    def __str__(self):
        return self.bio

    def profile_save(self):
        self.save()

    def profile_delete(self):
        self.delete()

    def update_profile(self):
        self.save()

    @classmethod
    def get_profile(cls,pk):
        profile = cls.objects.get(pk = pk)
        return profile 


        











