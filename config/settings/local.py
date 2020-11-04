from .base import *


DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'open_pdf_hosting',
        'USER': 'localdev',
        'PASSWORD': 'password1!',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# INSTALLED_APPS += ['debug_toolbar', ]

SECRET_KEY = 'jdyo34vh98yt359q7ytv99tv39ntv9n43qytm9werhtv9ueh'