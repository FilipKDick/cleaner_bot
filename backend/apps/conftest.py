import pytest

from pytest_factoryboy import register

from apps.users.tests.factories import UserFactory

register(UserFactory)


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath
