from bakery.custom_filebrowser.templatetags import get_file_extensions
from bakery.custom_filebrowser.sites import get_settings_var
from bakery.filebrowser_sites import firmware_site


class TestGetFileExtensions:

    def test_all(self):
        expected = []
        for _, extentions in firmware_site.extensions.items():
            expected += extentions
        context = dict(settings_var=get_settings_var('firmware'))
        assert sorted(get_file_extensions(context, '')) == sorted(expected)
