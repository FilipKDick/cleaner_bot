from datetime import timedelta

from django.utils import timezone

import factory

from factory import fuzzy  # noqa: WPS458 - need import colision, factory-boy's fault


class ChoreFactory(factory.django.DjangoModelFactory):
    owner = factory.SubFactory('apps.users.tests.factories.UserFactory')
    group = factory.SubFactory('apps.chores.tests.factories.ChoreGroupFactory')
    completion_period = fuzzy.FuzzyInteger(2, 14)
    last_completed_at = timezone.now() - timedelta(days=2)

    class Meta:
        model = 'chores.Chore'


class ChoreGroupFactory(factory.django.DjangoModelFactory):
    owner = factory.SubFactory('apps.users.tests.factories.UserFactory')

    class Meta:
        model = 'chores.ChoreGroup'
