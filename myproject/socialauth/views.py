# Create your views here.
from django.shortcuts import render, render_to_response
from django.contrib import auth
from socialauth.models import UserProfile
from django.http import HttpResponseRedirect
from django.utils.encoding import *
from  django.utils.http import *
import logging
logger = logging.getLogger(__name__)

def login(request):
    queryString = request.META['QUERY_STRING']
    queryStringEncode = urlquote(queryString)
    logger.debug("request: %s!" % queryStringEncode)
    return render_to_response("socialauth/login.html",{"user":request.user, "query_string":queryStringEncode})

def logged(request):
    return render_to_response("socialauth/logged.html",{"user":request.user})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login")