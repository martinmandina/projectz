from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project,profile

# Create your tests here.

class ProfileTestClass(TestCase):
    def setUp(self):
        self.newuser = User.objects.create_user(username='user',password='password')
        self.newprofile = Profile(id=1,prof_user=self.newuser,bio='add Bio',contacts='0721222222',profile_Id=1)
