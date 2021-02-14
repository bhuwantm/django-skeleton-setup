=================
SKELETON SETUPS
=================

A simple application to quickly setup settings files without too
much hassle.


Installation
-------------
``pip install django-skeleton-setup``



Quick start
-----------

1. Add "skeleton_setup" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'skeleton_setup',
    ]


2. If your application settings uses default WSGI_APPLICATION move to step 4 else to step 3


3. Set following variable to settings.py

   ``SKELETON_SITE_ROOT = Path(__file__).resolve().parent``


4. Run ``python manage.py skeleton_setup`` to create copy following files:

   * settings_common.py
   * settings_local.py
   * settings_production.py
   * env_local.env


5. Add following line to end of settings.py file

    ``from .settings_common import *``


6. Database setup is based on postgres, if other database is used then to avoid runserver error

    ``change DATABASES dict as required``


7. Change the following env file for local development

    ``env_local.env``


7. Edit env files or settings files as per your requirements
