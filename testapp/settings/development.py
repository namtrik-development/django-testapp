"""
Django settings for testapp project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7j6&2z2v5pl7om8z9jta+pcad(33m)*b7-6yj=*a68cm*4qq%8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
  }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# NOTE: las siguientes variables se configuraron para probar el despliegue mínimo del proyecto, es 
# decir, BD SQLite, datos precargados en la BD, etc.
ALLOWED_HOSTS = [
  'django-testapp-env.eba-zhzj2z22.us-east-1.elasticbeanstalk.com'
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
