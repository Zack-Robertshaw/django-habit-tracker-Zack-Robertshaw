from rest_framework import serializers
from core.models import Habit, Record

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

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = (
            'pk',
            'habit',
            'amount',
            'date',
            'created_at',
        )