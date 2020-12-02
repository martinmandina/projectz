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




