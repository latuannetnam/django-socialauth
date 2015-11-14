# django-socialauth

Django social authentication with Facebook, Google using python-social-auth

== Google API notes: to enable Google Authentiction, enable 2 API below:

* Google API: create client ID and secret
* Enable Google+ API (if don't add G+ then you will get the 403 Fobbiden Error)

== INSTALLATION

* pip install -r requirements.txt
* cd socialauth
* python manage.py syncdb
* python manage.py runserver ip:port
