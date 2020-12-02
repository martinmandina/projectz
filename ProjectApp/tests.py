from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project,Profile

# Create your tests here.

# Set up method
class ProfileTestClass(TestCase):
    def setUp(self):
        self.user_new = User.objects.create_user(username='user',password='passpass')
        self.profile_new = Profile(user_profile=self.user_new,bio='add Bio',contacts='0721222222',profile_Id=1)

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile_new,Profile))

# Testing Save Method
    def test_profile_save(self):
        self.profile_new.profile_save()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

# Testing delete Method
    def test_profile_delete(self):
        self.profile_new.profile_save()
        profiles = Profile.objects.all()
        self.profile_new.profile_delete()
        self.assertTrue(len(profiles) == 0)

# Set up method
class ProjectTestClass(TestCase):
    def setUp(self):
        self.user_new = User.objects.create_user(username='user',password='passpass')
        self.profile_new = Profile(user_profile=self.user_new,bio='add Bio',contacts='0721222222',profile_Id=1)
        self.profile_new.profile_save()
        self.project_new = Project(id=1,title='title',description='description',link='www.mimi.com',user=self.user_new)

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.project_new,Project))

# Testing Save Method
    def test_save_project(self):
        self.project_new.project_save()
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)

# Testing delete Method
    def test_profile_delete(self):
        self.project_new.project_delete()
        projects = Project.objects.all()
        self.assertTrue(len(projects)==0)

# Testing search method
def test_find_project(self):
        self.project_new.project_save()
        project = Project.find_project(self.project_new.id)
        self.assertTrue(project == self.project_new)



  


    

   






    



