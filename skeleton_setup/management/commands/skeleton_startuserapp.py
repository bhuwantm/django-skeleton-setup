import os
import sys
from pathlib import Path

from django.template import Context

from skeleton_setup.management.commands import skeleton_startapp


class Command(skeleton_startapp.Command):
    help = '''
        Minimal command equivalent to django-admin startapp for skeleton user app structure.
        Dependency: djangorestframework
    '''

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.model_name = None
        self.model_table = None

    def get_template_context(self, app_name, *args, **options):
        camel_case_value = ''.join(x for x in app_name.title() if x != '_')
        context = Context({
            **options,
            'app_name': app_name,
            'camel_case_app_name': camel_case_value,
            'model_name': self.model_name,
            'model_table': self.model_table,
        }, autoescape=False)
        return context

    def get_source_path(self):
        current_app_path = Path(__file__).resolve().parent.parent.parent
        source_path = os.path.join(current_app_path, 'conf/user_template')
        return source_path

    def handle(self, *args, **options):
        try:
            while self.model_name is None:
                self.model_name = input("User model name (UpperCamelCase): ")
                if not self.model_name:
                    self.stderr.write("Model name is required and cannot be blank.")
                    self.model_name = None

            while self.model_table is None:
                self.model_table = input("Table name for user model (snake_case) [Optional]: ")

        except KeyboardInterrupt:
            self.stderr.write("\nOperation cancelled.")
            sys.exit(1)

        super(Command, self).handle(*args, **options)
