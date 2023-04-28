import datetime
import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from apps.chores.enums import ChoreCompletionStatus

User = get_user_model()


class ChoreHistory(models.Model):
    chore = models.ForeignKey(
        'chores.Chore',
        on_delete=models.CASCADE,
        related_name='history',
    )
    finished_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.chore} finished at {self.finished_at: %Y/%m/%d}'


class Chore(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=128)
    group = models.ForeignKey(
        'chores.ChoreGroup',
        on_delete=models.CASCADE,
        related_name='chores',
    )
    completion_frequency = models.IntegerField(
        help_text='How often (days) should it be done',
    )
    last_completed_at = models.DateTimeField()

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if 'last_completed_at' in kwargs.get('update_fields', []):
            ChoreHistory.objects.create(chore=self)

    @property
    def due_soon_date(self) -> datetime.datetime:
        soon_days = int(self.completion_frequency * 0.7)
        return self.last_completed_at + datetime.timedelta(days=soon_days)

    @property
    def due_date(self) -> datetime.datetime:
        due_days = self.completion_frequency
        return self.last_completed_at + datetime.timedelta(days=due_days)

    @property
    def overdue_date(self) -> datetime.datetime:
        overdue_days = 2 * self.completion_frequency
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

    def mark_done(self):
        self.last_completed_at = timezone.now()
        self.save(update_fields=['last_completed_at'])


class ChoreGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

    def status(self):
        chores = self.chores.all()
        if any(chore.status == ChoreCompletionStatus.OVERDUE.value for chore in chores):
            return ChoreCompletionStatus.OVERDUE.value
        if any(chore.status == ChoreCompletionStatus.DUE.value for chore in chores):
            return ChoreCompletionStatus.DUE.value
        if any(chore.status == ChoreCompletionStatus.SOON.value for chore in chores):
            return ChoreCompletionStatus.SOON.value
        return ChoreCompletionStatus.SAFE.value


class ChorePage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    # TODO: default name
    name = models.CharField(max_length=128)
    groups = models.ManyToManyField('chores.ChoreGroup', related_name='pages')

    def __str__(self) -> str:
        return self.name
