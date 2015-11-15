from django.contrib import admin

# Register your models here.
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('backend','username', 'fullname', 'email')
    #fields = ['username', 'fullname', 'email']

admin.site.register(UserProfile,UserProfileAdmin)