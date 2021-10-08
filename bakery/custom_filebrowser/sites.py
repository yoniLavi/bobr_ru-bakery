import wrapt
from filebrowser.sites import FileBrowserSite as BaseFileBrowserSite
from django.core.files.storage import default_storage


# registry of custom sites, identified by directory
registry = {}


class FileBrowserSite(BaseFileBrowserSite):
    """Improved file browser site, with custom directory, file types."""

    def __init__(self, name=None, app_name='bakery.custom_filebrowser', storage=default_storage,
                 directory=None,
                 extensions=None,
                 select_formats=None):
        super().__init__(name, app_name, storage)
        self.directory = directory or ''
        self.extensions = extensions or {}
        self.select_formats = select_formats or {}

        # TODO: check if exists (optional)
        registry[self.directory] = self


@wrapt.patch_function_wrapper('filebrowser.sites', 'get_settings_var')
def get_settings_var(wrapped, instance, args, kwargs):
    settings_var = wrapped(*args, **kwargs)
    # TODO: override if kwargs['directory'] is found in registry
    return settings_var


@wrapt.patch_function_wrapper('filebrowser.base', 'FileObject._get_file_type')
def get_file_type(wrapped, instance, args, kwargs):
    file_type = wrapped(*args, **kwargs)
    # TODO: override if instance.site is a custom filebrowser
    return file_type


@wrapt.patch_function_wrapper('filebrowser.base', 'FileObject._get_format_type')
def get_format_type(wrapped, instance, args, kwargs):
    format_type = wrapped(*args, **kwargs)
    # TODO: override if instance.site is a custom filebrowser
    return format_type
