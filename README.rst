=================
SKELETON SETUPS
=================

A simple application to quickly setup settings files without too
much hassle.


Configure Settings and Environment Files
-----------------------------------------

1. Add "skeleton_setup" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'skeleton_setup',
    ]


2. If your application settings uses default WSGI_APPLICATION move to step 4 else to step 3


3. Set following variable to settings.py.

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


Creating a new app provided by skeleton setup
----------------------------------------------

1. Minimal command similar to startapp of django-admin

    ``python manage.py skeleton_startapp app_name to_path``


2. Parameter "app_name" is required


3. Parameter "to_path" is optional and is path string value relative to BASE_DIR where
   you want to create the app


Don't like app structure provided by this?
--------------------------------------------

1. No problem you can create your own app structure and use this command

2. Create a template structure for your application.
   Use `"*.py-tpl"` instead of ``"*.py"`` files.

3. Add following variable to settings.py

    ``SKELETON_STARTAPP_SOURCE="path/to/your/template/"``

4. If you still want to have finer control over the app creation. Extend the following class:

    sleleton_startapp.Command