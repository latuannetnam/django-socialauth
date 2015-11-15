# django-socialauth

Django social authentication with Facebook, Google using python-social-auth

## Google API notes: to enable Google Authentication, enable 2 API below:
* Google API: create client ID and secret
* Enable Google+ API (if don't add G+ then you will get the 403 Fobbiden Error)

## Features:
* Facebook authentication (Done)
* Google authentication (Done)
* Twitter authentication
* Auto user creation with social account (Done)
* Save GET/POST parameter of original page (Partion done via key parameter)
* Get social profile: email, photo (Done with Facebook, Google)

## INSTALLATION
* pip install -r requirements.txt
* cd myproject
* python manage.py syncdb
* python manage.py runserver ip:port
