from django.urls import (
    resolve,
    reverse,
)

from apps.users.models import User


def test_user_detail(db: None, user: User):
    assert (
        reverse('users:user-detail', kwargs={'username': user.username})
        == f'/api/v1/users/{user.username}/'
    )
    assert resolve(f'/api/v1/users/{user.username}/').view_name == 'users:user-detail'


def test_user_list():
    assert reverse('users:user-list') == '/api/v1/users/'
    assert resolve('/api/v1/users/').view_name == 'users:user-list'


def test_user_me():
    assert reverse('users:user-me') == '/api/v1/users/me/'
    assert resolve('/api/v1/users/me/').view_name == 'users:user-me'
