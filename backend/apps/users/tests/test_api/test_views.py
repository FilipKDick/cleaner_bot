import typing

from django.urls import reverse

from apps.users.models import User

if typing.TYPE_CHECKING:
    from django.test.client import Client


class TestUserViewSet:
    def test_get_queryset(self, db: None, user: User, client: 'Client'):
        client.force_login(user)
        url = reverse('users:user-detail', kwargs={'username': user.username})
        response = client.get(url)
        assert response.json() == {
            'username': user.username,
            'name': user.name,
        }

    def test_me(self, db: None, user: User, client: 'Client'):
        client.force_login(user)
        url = reverse('users:user-me')
        response = client.get(url)

        assert response.json() == {
            'username': user.username,
            'name': user.name,
        }
