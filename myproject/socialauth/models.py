from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, related_name='profile')
    photo = models.TextField(null=True)
    key  = models.TextField(null=True)
