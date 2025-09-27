from mysite.settings import *
import os
from decouple import config

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['travelistaa.ir', 'www.travelistaa.ir']

# INSTALLED_APPS = []

# sites framework
SITE_ID = 2

# MIDDLEWARE = [
# ]



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config("MYSQL_DATABASE"),
        'USER': config("MYSQL_USER"),
        'PASSWORD': config("MYSQL_PASSWORD"),
        'HOST': config("MYSQL_HOST"),
        'PORT': config("MYSQL_PORT"),
    }
}


STATIC_ROOT = '/home/traveli1/public_html/static'
MEDIA_ROOT = '/home/traveli1/public_html/media'


STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True

#X-Content-Type-Options
SECURE_CONTENT_TYPE_NOSNIFF = True

## Strict-Transport-Security
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

## that requests over HTTP are redirected to HTTPS. aslo can config in webserver
SECURE_SSL_REDIRECT = True 

# for more security
CSRF_COOKIE_SECURE = True
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Strict'




EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.travelistaa.ir'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_DJANGO_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_DJANGO_PASSWORD')
DEFAULT_FROM_EMAIL = config('EMAIL_DJANGO_USER')


