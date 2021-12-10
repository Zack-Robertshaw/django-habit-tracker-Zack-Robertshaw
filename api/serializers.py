from django.db.models import fields
from rest_framework import serializers
from core.models import Habit, Record
from django.contrib.auth.models import User



# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = (all)

class RecordsForHabitSerializer(serializers.ModelSerializer):
    class  Meta:
        Model = Record
        fields = ("amount",
                "date",)


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = (
            'pk',
            'user',
            'habit',
            'amount',
            'date',
            'created_at',
        )

class HabitSerializer(serializers.ModelSerializer):
    records = RecordSerializer(many=True)
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
            'records',
        )
    
