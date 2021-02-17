import os

from django.core import management


class Command(management.BaseCommand):
    help = 'Copies settings files to main app and local env file to base directory.'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        import shutil
        from django.conf import settings
        from pathlib import Path

        current_app_path = Path(__file__).resolve().parent.parent.parent
        site_root = getattr(settings, 'SKELETON_SITE_ROOT', None)
        if not site_root:
            # assuming recommendation project structure is used
            # try to use WSGI_APPLICATION to get app_name if SKELETON_SITE_ROOT is not present
            app_name = settings.WSGI_APPLICATION.split('.')[0]
            site_root = os.path.join(settings.BASE_DIR, app_name)

        settings_common_path = os.path.join(current_app_path, 'settings_common.py')
        settings_local_path = os.path.join(current_app_path, 'settings_local.py')
        settings_production_path = os.path.join(current_app_path, 'settings_production.py')
        env_local_path = os.path.join(current_app_path, 'env_local.env')

        shutil.copy(settings_common_path, site_root)
        self.stdout.write(self.style.SUCCESS("Successfully copied settings_common.py."))

        shutil.copy(settings_local_path, site_root)
        self.stdout.write(self.style.SUCCESS("Successfully copied settings_local.py."))

        shutil.copy(settings_production_path, site_root)
        self.stdout.write(self.style.SUCCESS("Successfully copied settings_production.py."))

        shutil.copy(env_local_path, settings.BASE_DIR)
        self.stdout.write(self.style.SUCCESS("Successfully copied env_local.env to base directory."))
