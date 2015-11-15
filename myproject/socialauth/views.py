# Create your views here.
from django.shortcuts import render, render_to_response
from django.contrib import auth
from socialauth.models import UserProfile
from django.http import HttpResponseRedirect
import logging
logger = logging.getLogger(__name__)

def login(request):
    logger.debug("user: %s!" % request.user)
    return render_to_response("socialauth/login.html",{"user":request.user})

def logged(request):
    return render_to_response("socialauth/logged.html",{"user":request.user})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login")