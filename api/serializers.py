from django.db.models import fields
from rest_framework import serializers
from core.models import Habit, Record
from django.contrib.auth.models import User



# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User

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
            'user',
            'habit',
            'amount',
            'date',
            'created_at',
        )