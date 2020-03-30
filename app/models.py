from django.db import models
from django.contrib.auth.models import User
from social.apps.django_app.default.models import UserSocialAuth
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    skills = models.CharField(max_length=255, null=True, blank=True)
    file = models.FileField(upload_to='media')



class Document(models.Model):
    file = models.FileField(upload_to='media')

