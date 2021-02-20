import os

import socket

from pathlib import Path

# host machine name
HOSTNAME = socket.gethostname()

# Main path setups
BASE_DIR = Path(__file__).resolve().parent.parent
LOCALE_DIR = os.path.join(BASE_DIR, 'locale')
EXTRA_DIR = os.path.join(BASE_DIR, 'extras')
STATIC_DIR = os.path.join(EXTRA_DIR, 'static')
MEDIA_DIR = os.path.join(EXTRA_DIR, 'media')

# environ setup for boolean true strings
BOOLEAN_TRUE_STRINGS = ('true', 'True', 'Yes', 'yes')

# model which is to be used as a user model, change as per required
# AUTH_USER_MODEL = 'app_user.AppUser'  # CHANGE RECOMMENDED

# total number of fields that a request can have
DATA_UPLOAD_MAX_NUMBER_FIELDS = 2000

# A list of directories where Django looks for translation files
LOCALE_PATHS = [LOCALE_DIR]

# login and redirect after login setting, change it as required
LOGIN_REDIRECT_URL = '/'  # CHANGE RECOMMENDED
LOGIN_URL = '/login/'  # CHANGE RECOMMENDED

# STATIC FILE SETTINGS
STATIC_URL = '/static/'
STATIC_ROOT = STATIC_DIR
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# MEDIA FILES SETTING
MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_DIR

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 9,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    }
]

# EMAIL SETTINGS, remove if not required
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST = 'mtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 465
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# patterns of date format that are accepted by our application
DATE_INPUT_FORMATS = [
    '%Y-%m-%d',
    '%m/%d/%Y',
    '%m/%d/%y',
    '%d/%m/%Y'
]

# django rest framework settings, remove if not required
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DATE_INPUT_FORMATS': DATE_INPUT_FORMATS,
    'COERCE_DECIMAL_TO_STRING': False,
}

"""
ENVIRONMENT SELECTION AND CORRESPONDING FILE LOADING
"""
IS_PROD = False
IS_LOCAL = True

# ensures that only one env bool value is true
ENV_LIST_BOOL = [IS_PROD, IS_LOCAL]
init_bool = False
for each in ENV_LIST_BOOL:
    if each and init_bool:
        raise ValueError('Repeat value for env bool detected.')
    elif each and not init_bool:
        init_bool = True

if IS_PROD:
    from .settings_production import *

if IS_LOCAL:
    from .settings_local import *
"""
END OF ENVIRONMENT SELECTION AND CORRESPONDING FILE LOADING
"""
