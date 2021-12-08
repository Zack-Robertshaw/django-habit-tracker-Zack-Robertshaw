from rest_framework import serializers
from core.models import Habit

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = (
            'pk',
            'user',
            'name',
            'goal',
            'goal_unit',
            'duration',
            'created_at',
        )