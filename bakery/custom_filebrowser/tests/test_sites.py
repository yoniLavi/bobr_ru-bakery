from django.urls import reverse


class TestFileBrowserSite:

    def test_browse(self, admin_client):
        url = reverse('firmware:fb_browse')
        response = admin_client.get(url)
        assert response.status_code == 200

    # TODO: add tests based on
    # https://github.com/sehmaschine/django-filebrowser/blob/master/tests/test_sites.py
