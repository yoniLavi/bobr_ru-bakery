import pytest

import os

from bakery.users.models import User
from bakery.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath
    os.makedirs(os.path.join(tmpdir.strpath, 'firmware'))


@pytest.fixture
def user() -> User:
    return UserFactory()
