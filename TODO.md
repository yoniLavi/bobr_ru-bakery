This project is based on Django Cookiecutter https://github.com/pydanny/cookiecutter-django,
which brings docker-compose setups for development/production. Run locally:

    $ docker-compose -f local.yml up

and open http://localhost:8000 in browser. Local setup mount the working
directory so that any changes will be reflected in the browser.

The initial project is extended by grappelli/dashboard/filebrowser modules.
Grappelli is a popular admin skin, with simple dashboard and filebrowser
modules. Usually, filebrowser module is used in combination with Grappelli
TinyMCE editor to customise admins for models with rich text, for example,
django.contrib.flatpages.

We would like to reuse its functionality to store files of different types
in separate storages (subdirectories of django media). What is required:

1. Add multi-site support to django-filebrowser by patching and extending
   so that each site has its own (bakery/custom_filebrowser/sites.py):
   - storage (subdirectory in media),
   - file types/extensions.
2. In addition to the standard file browser for media files in the dashboard,
   add a firmwate site to mamage tarballs.
3. Test the new features.
   Probably, it would be more accurate to integrate original tests as well:
   https://github.com/sehmaschine/django-filebrowser/tree/master/tests
   (sorry for mismatch of testing frameworks)

For rapid/safe patching I recommend wrapt by Graham Dumpleton
https://github.com/GrahamDumpleton/wrapt. He made several interesting talks
on wrapt applications, for example https://youtu.be/uJZKj_igMh4.

Refer .gitlab-ci.yml to prepare local dev environment.
