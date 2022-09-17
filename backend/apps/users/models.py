from django.contrib.auth.models import AbstractUser
from django.db.models import CharField


class User(AbstractUser):
    """Default custom user model for Cleaner Bot."""

    name = CharField('Name of the User', blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
