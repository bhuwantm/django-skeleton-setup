import os

import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, 'env_local.env')
env = environ.Env()
env.read_env(ENV_PATH)

SECRET_KEY = env('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['*']

# DB settings, CHANGE RECOMMENDED
DB_NAME = env('DB_NAME')
DB_USER = env('DB_USER')
DB_PASS = env('DB_PASS')
DB_HOST = env('DB_HOST')
DB_PORT = env('DB_PORT')
ATOMIC_REQUEST = env.bool('ATOMIC_REQUEST')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
        'ATOMIC_REQUESTS': ATOMIC_REQUEST
    }
}

# AutoBackend added which always login the first user in the User table
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'skeleton_setup.backends.EmailBackend',
    'skeleton_setup.backends.AutoBackend'
]
