from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    #user = models.ForeignKey(User, unique=True, related_name='profile')
    user = models.OneToOneField(User, related_name='profile')
    username=  models.TextField(null=True)
    fullname = models.TextField(null=True)
    last_name = models.TextField(null=True)
    first_name= models.TextField(null=True)
    photo = models.TextField(null=True)
    email = models.TextField(null=True)
    key  = models.TextField(null=True)
    backend = models.TextField(null=True)

