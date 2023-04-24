from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import (
    Chore,
    ChoreGroup,
    ChorePage,
)


class ChoreDateField(serializers.DateTimeField):
    def __init__(self, default_timezone=None, **kwargs):
        date_format = '%Y/%m/%d'
        input_formats = ['%Y/%m/%dT%H:%M:%S', date_format]
        super().__init__(date_format, input_formats, default_timezone, **kwargs)


class ChoreSerializer(serializers.ModelSerializer):
    group_id = serializers.UUIDField()
    last_completed_at = ChoreDateField()
    due_date = ChoreDateField()

    class Meta:
        model = Chore
        fields = [
            'id',
            'name',
            'status',
            'completion_frequency',
            'last_completed_at',
            'group_id',
            'due_date',
        ]

    def validate_group_id(self, group_id):
        try:
            ChoreGroup.objects.get(id=group_id)
        except ChoreGroup.DoesNotExist:
            raise ValidationError(f'Chore group {group_id} does not exist')
        return group_id


class ChoreGroupSerializer(serializers.ModelSerializer):
    chores = ChoreSerializer(many=True)

    class Meta:
        model = ChoreGroup
        fields = ['id', 'name', 'chores', 'status']


class ChorePageSerializer(serializers.ModelSerializer):
    groups = ChoreGroupSerializer(many=True)

    class Meta:
        model = ChorePage
        fields = ['id', 'name', 'groups']
