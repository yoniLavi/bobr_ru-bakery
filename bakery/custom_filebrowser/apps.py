from django.apps import AppConfig


class CustomAdminConfig(AppConfig):
    name = 'bakery.custom_filebrowser'

    def ready(self):
        from . import forms  # noqa
