import os
import shutil
import stat
from importlib import import_module
from pathlib import Path

from django.conf import settings
from django.core import management
from django.core.management import CommandError
from django.template import Context, Engine


class Command(management.BaseCommand):
    help = 'Minimal command equivalent to django-admin startapp for skeleton app structure.'

    REWRITE_TEMPLATE_SUFFIXES = (
        # Allow shipping invalid .py files without byte-compilation.
        ('.py-tpl', '.py'),
    )

    WRITABLE_EXTENSION = ('.py',)

    IGNORE_FILES = ('*.pyo', '*.pyc', '*.py.class', 'tmp')

    def add_arguments(self, parser):
        parser.add_argument('app_name', help='Name of the application.')
        parser.add_argument(
            'to_path',
            help='Path as string relative to base directory where you want to create the new app.',
            default='',
            nargs='?',
            type=str
        )

    def get_template_context(self, app_name, *args, **options):
        camel_case_value = ''.join(x for x in app_name.title() if x != '_')
        context = Context({
            **options,
            'app_name': app_name,
            'camel_case_app_name': camel_case_value,
        }, autoescape=False)
        return context

    def get_source_path(self):
        source_path = getattr(settings, 'SKELETON_STARTAPP_SOURCE', None)
        if source_path is None:
            current_app_path = Path(__file__).resolve().parent.parent.parent
            source_path = os.path.join(current_app_path, 'conf/app_template')
        return source_path

    def handle(self, app_name, to_path, *args, **options):
        self.validate_name(app_name)
        context = self.get_template_context(app_name, *args, **options)

        source_path = self.get_source_path()
        destination_path = os.path.join(settings.BASE_DIR, to_path, app_name)

        # copying template files to destination folder
        shutil.copytree(source_path, destination_path, ignore=shutil.ignore_patterns(*self.IGNORE_FILES))

        for root, dirs, files in os.walk(destination_path):
            for filename in files:
                # replacing old extension with mapped extension from "REWRITE_TEMPLATE_SUFFIXES"
                for old_suffix, new_suffix in self.REWRITE_TEMPLATE_SUFFIXES:
                    old_filename = filename
                    if old_filename.endswith(old_suffix):
                        new_filename = old_filename[:-len(old_suffix)] + new_suffix
                        os.rename(os.path.join(root, old_filename), os.path.join(root, new_filename))
                        break  # Only rewrite once

        for root, dirs, files in os.walk(destination_path):
            for filename in files:
                file_path = os.path.join(root, filename)

                try:
                    self.make_writeable(file_path)
                except OSError:
                    self.stderr.write(
                        "Notice: Couldn't set permission bits on %s. You're "
                        "probably using an uncommon filesystem setup. No "
                        "problem." % file_path, self.style.NOTICE)

                # Only render the Python files, as we don't want to
                # accidentally render Django templates files
                if file_path.endswith(self.WRITABLE_EXTENSION):
                    with open(file_path, mode='r+', encoding='utf-8') as new_file:
                        content = new_file.read()
                        template = Engine().from_string(content)
                        content = template.render(context)
                        new_file.seek(0)
                        new_file.truncate()
                        new_file.write(content)

    # same function used by django startapp
    def validate_name(self, name):
        if name is None:
            raise CommandError('you must provide app name')

        # Check it's a valid directory name.
        if not name.isidentifier():
            raise CommandError(
                "'{name}' is not a valid app name. Please make sure given name is a valid identifier.".format(
                    name=name
                )
            )

        # Check it cannot be imported.
        try:
            import_module(name)
        except ImportError:
            pass
        else:
            raise CommandError(
                "'{name}' conflicts with the name of an existing Python "
                "module and cannot be used as app name.".format(
                    name=name
                )
            )

    # same function used by django startapp
    def make_writeable(self, filename):
        """
        Make sure that the file is writeable.
        Useful if our source is read-only.
        """
        if not os.access(filename, os.W_OK):
            st = os.stat(filename)
            new_permissions = stat.S_IMODE(st.st_mode) | stat.S_IWUSR
            os.chmod(filename, new_permissions)
