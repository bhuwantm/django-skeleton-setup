=================
SKELETON SETUPS
=================

A simple application to quickly setup settings files without too
much hassle.


Quick start
-----------

1. Add "skeleton_setups" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'skeleton_setups',
    ]


2. If your application settings uses default WSGI_APPLICATION move to step 4 else to step 3


3. Set following variable to settings.py

   ``SKELETON_SITE_ROOT = Path(__file__).resolve().parent``


4. Run ``python manage.py skeleton_setups`` to create copy following files:

   * settings_common.py
   * settings_local.py
   * settings_production.py
   * env_local.env


5. Add following line to end of settings.py file

    ``from settings_common import *``


6. Edit settings files as per your requirements