import datetime
import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from apps.chores.enums import ChoreCompletionStatus

User = get_user_model()


class Chore(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=128)
    group = models.ForeignKey(
        'chores.ChoreGroup',
        on_delete=models.CASCADE,
        related_name='chores',
    )
    completion_period = models.IntegerField(
        help_text='How often (days) should it be done',
    )
    last_completed_at = models.DateTimeField()

    def __str__(self) -> str:
        return self.name

    @property
    def due_soon_date(self) -> datetime.datetime:
        soon_days = int(self.completion_period * 0.7)
        return self.last_completed_at + datetime.timedelta(days=soon_days)

    @property
    def due_date(self) -> datetime.datetime:
        due_days = self.completion_period
        return self.last_completed_at + datetime.timedelta(days=due_days)

    @property
    def overdue_date(self) -> datetime.datetime:
        overdue_days = 2 * self.completion_period
        return self.last_completed_at + datetime.timedelta(days=overdue_days)

    @property
    def status(self) -> str:
        now = timezone.now()
        if now < self.due_soon_date:
            return ChoreCompletionStatus.SAFE.value
        if now < self.due_date:
            return ChoreCompletionStatus.SOON.value
        if now < self.overdue_date:
            return ChoreCompletionStatus.DUE.value
        return ChoreCompletionStatus.OVERDUE.value


class ChoreGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=128)
    page = models.ForeignKey(
        'chores.ChorePage',
        on_delete=models.CASCADE,
        related_name='groups',
    )

    def __str__(self) -> str:
        return self.name


class ChorePage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    # TODO: default name
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name
