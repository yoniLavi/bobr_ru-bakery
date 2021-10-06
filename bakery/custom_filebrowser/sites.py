# TODO (for me): elaborate more on this

from filebrowser import sites as fb_sites


class FileBrowserSite(fb_sites.FileBrowserSite):
    """Improved file browser site custom subdirectory, file types, views permission."""

    @property
    def admin_url_regex(self):
        return r'^filebrowser/{}/'.format(self.name)

    EXTENSIONS = {}

    perm = None
