from bakery.custom_filebrowser.sites import FileBrowserSite
from filebrowser.sites import site as default_site  # noqa


firmware_site = FileBrowserSite(
    name='firmware',
    directory='firmware',
    extensions={
        'Tarball': ['.tar', '.tgz'],
        'Package': ['.deb', '.rpm'],
    },
    select_formats={
        'Firmware': ['Tarball', 'Package'],
    })
