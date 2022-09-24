from rest_framework import serializers

from .models import (
    Chore,
    ChoreGroup,
    ChorePage,
)


class ChoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chore
        fields = ['id', 'name', 'status']


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
