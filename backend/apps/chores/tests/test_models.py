import pytest

from .factories import ChoreFactory


@pytest.mark.django_db
class TestChore:
    def test_chore_string_is_its_name(self):
        name = 'test name'
        chore = ChoreFactory(name=name)
        assert str(chore) == name
