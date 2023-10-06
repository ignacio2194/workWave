from base import *

import os
import dj_database_url

ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(',')

CLOUDINARY_URL = env('CLOUDINARY_URL')

DATABASES = {
    'default': dj_database_url.config(
        default = os.environ.get('DATABASE_URL')
    )
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}


AUTH_PASSWORD_VALIDATORS += [
    {
        "NAME": "workwave.apps.users.validators.CustomPasswordValidator",
    },
]

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

#Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD') 
EMAIL_PORT = env('EMAIL_PORT')

STATIC_ROOT = BASE_DIR / 'static'
