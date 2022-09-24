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
    def status(self):
        soon_days = int(self.completion_period * 0.7)
        due_days = self.completion_period
        overdue_days = 2 * self.completion_period
        soon_date = self.last_completed_at + datetime.timedelta(days=soon_days)
        due_date = self.last_completed_at + datetime.timedelta(days=due_days)
        overdue_date = self.last_completed_at + datetime.timedelta(days=overdue_days)
        now = timezone.now()
        if now < soon_date:
            return ChoreCompletionStatus.SAFE.value
        if now < due_date:
            return ChoreCompletionStatus.SOON.value
        if now < overdue_date:
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
