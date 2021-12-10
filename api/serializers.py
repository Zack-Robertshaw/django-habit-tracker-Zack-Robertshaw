from django.db.models import fields
from rest_framework import serializers
from core.models import Habit, Record
from django.contrib.auth.models import User



# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = (all)

# class RecordsForHabitSerializer(serializers.ModelSerializer):
#         habit = serializers.StringRelatedField()
#     class  Meta:
#         Model = Record
#         fields = (
#                 'habit'
#                 'amount',
#                 'date',)


class RecordSerializer(serializers.ModelSerializer):
        # habit = serializers.StringRelatedField(read_only=True)
        # user = serializers.StringRelatedField(read_only=True)

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
    # pk = RecordSerializer(read_only=True)
    records = RecordSerializer(many=True, read_only=True)
    # user = serializers.StringRelatedField()
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
    
