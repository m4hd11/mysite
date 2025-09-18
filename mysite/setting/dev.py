from mysite.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)2l4mi(1f(kv)4(v(7f*-=(v8p_re6ez+vg9j#_d%#zqqn*tqg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['410cb00f12fb.ngrok-free.app', 'localhost', '127.0.0.1']



# INSTALLED_APPS = []


# sites framework
SITE_ID = 2


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'


STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

X_FRAME_OPTIONS = 'SAMEORIGIN'

# CSRF_TRUSTED_ORIGINS = ['https://410cb00f12fb.ngrok-free.app']

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'mail.travelistaa.ir'
# EMAIL_PORT = 465
# EMAIL_USE_SSL = True
# EMAIL_USE_TLS = False
# EMAIL_HOST_USER = 'no-reply@travelistaa.ir'
# EMAIL_HOST_PASSWORD = 'h3hJcJa$a6dx'
# DEFAULT_FROM_EMAIL = 'no-reply@travelistaa.ir'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'mahdi.irp.pv@gmail.com'
EMAIL_HOST_PASSWORD = 'kpmajciapsuntybe'
DEFAULT_FROM_EMAIL = 'mahdi.irp.pv@gmail.com'

