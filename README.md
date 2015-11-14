# django-socialauth

Django social authentication with Facebook, Google using python-social-auth

## Google API notes: to enable Google Authentiction, enable 2 API below:
* Google API: create client ID and secret
* Enable Google+ API (if don't add G+ then you will get the 403 Fobbiden Error)

## Features:
* Facebook authenticaton (Done)
* Google authenticaton (Done)
* Twitter authenticaton 
* Auto user creation with social account (Done)
* Save GET/POST parameter of original page
* Get social profile: email, photo

## INSTALLATION
* pip install -r requirements.txt
* cd socialauth
* python manage.py syncdb
* python manage.py runserver ip:port
