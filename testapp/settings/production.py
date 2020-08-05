"""
Django settings for testapp project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

from .base import *
from .ebutils import LOG_PATH, get_instance_ip

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*h8c4)@8@vd4&j%i8gtegq)kw_xjum^6u(=g@b$nh&syirbc=k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
  'django-testapp-env.eba-s9rznadh.us-east-1.elasticbeanstalk.com',
  'testapp.namtrik.dev',
]

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': os.environ['RDS_DB_NAME'],
    'USER': os.environ['RDS_USERNAME'],
    'PASSWORD': os.environ['RDS_PASSWORD'],
    'HOST': os.environ['RDS_HOSTNAME'],
    'PORT': os.environ['RDS_PORT']
  }
}

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 3600

# LOG_FILENAME = os.path.join(LOG_PATH, 'app.log')
# LOGGING = {
#   'version': 1,
#   'disable_existing_loggers': False,
#   'formatters': {
#     'file': {
#       'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
#     }
#   },
#   'handlers': {
#     'file': {
#       'level': 'WARNING',
#       'class': 'logging.FileHandler',
#       'filename': LOG_FILENAME,
#     },
#     'mail_admins': {
#       'level': 'ERROR',
#       'class': 'django.utils.log.AdminEmailHandler',
#       'include_html': True,
#     }
#   },
#   'loggers': {
#     'django': {
#       'handlers': ['file', 'mail_admins'],
#       'level': 'DEBUG',
#       'propagate': True,
#     }
#   },
# }

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

INSTANCE_PRIVATE_IP = get_instance_ip()
ALLOWED_HOSTS.append(INSTANCE_PRIVATE_IP)
