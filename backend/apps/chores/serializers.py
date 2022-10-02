from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import (
    Chore,
    ChoreGroup,
    ChorePage,
)


class ChoreSerializer(serializers.ModelSerializer):
    group_id = serializers.UUIDField()

    class Meta:
        model = Chore
        fields = [
            'id',
            'name',
            'status',
            'completion_period',
            'last_completed_at',
            'group_id',
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
        fields = ['id', 'name', 'chores']


class ChorePageSerializer(serializers.ModelSerializer):
    groups = ChoreGroupSerializer(many=True)

    class Meta:
        model = ChorePage
        fields = ['id', 'name', 'groups']
