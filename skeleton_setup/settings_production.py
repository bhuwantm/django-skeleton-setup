import os
import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, 'env_production.env')
env = environ.Env()
env.read_env(ENV_PATH)

SECRET_KEY = env('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

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

# Email Settings, remove if not required
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

# Security
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
