from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from core.models import Habit
from .serializers import HabitSerializer

# Create your views here.
class HabitListView(ListAPIView):

    # list all habits

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    #  def get(self, request, format=None):
        
    #     # create a response that includes a list of habits
    #     habits = Habit.objects.all() 
    #     serializer = HabitSerializer(habits, many=True)

    #     return Response(serializer.data)

class HabitDetailView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
