=================
SKELETON SETUPS
=================

A simple application to quickly setup settings files without too
much hassle.

Installation
-------------
    ``pip install django-skeleton-setup``


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

4. App with following structure will be created::

    ├── api
    │   ├── __init__.py
    │   ├── urls.py
    │   └── views.py
    ├── migrations
    │   └── __init__.py
    ├── serializers
    │   └── __init__.py
    ├── services
    │   └── __init__.py
    ├── templates
    ├── tests
    │   └── __init__.py
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── model_managers.py
    ├── models.py
    ├── signals.py
    └── urls.py
    └── utils.py
    └── views.py


Don't like app structure provided by this?
--------------------------------------------

1. No problem you can create your own app structure and use this command

2. Create a template structure for your application.
   Use `"*.py-tpl"` instead of ``"*.py"`` files.

3. Example template::

    ├── api
    │   ├── __init__.py-tpl
    │   ├── urls.py
    │   └── views.py
    ├── migrations
    │   └── __init__.py-tpl
    ├── tests
    │   └── __init__.py-tpl
    ├── utils
    │   └── __init__.py-tpl
    ├── static
    │   └── assets
    │   └── js
    │   └── css
    ├── templates
    ├── admin.py-tpl
    ├── apps.py-tpl
    ├── models.py-tpl
    └── urls.py-tpl
    └── views.py-tpl


4. Add following variable to settings.py

    ``SKELETON_STARTAPP_SOURCE="path/to/your/template/"``

5. If you still want to have finer control over the app creation. Extend the following class:

    skeleton_startapp.Command




Creating a user app
----------------------

DEPENDENCIES: djangorestframework

Creates an app for handling users.

1. Command similar to startapp of django-admin

    ``python manage.py skeleton_startuserapp app_name to_path``

2. The command prompts for::

    UserModel [Suggestion: UpperCamelCase]

    db_table [Suggestion: snake_case] [Optional]

3. An app is created with given app_name

3. Modify the app as required

4. Add it to INSTALLED_APPS in settings.py

5. Make migrations and migrate
