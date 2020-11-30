from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    image = models.ImageField(upload_to='picha',blank=True,null=True)
    link = models.URLField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

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
    def get_one_project(cls,pk):
        project = cls.objects.get(pk = pk)
        return project 

        






