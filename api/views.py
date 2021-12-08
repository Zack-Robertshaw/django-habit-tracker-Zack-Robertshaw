from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from core.models import Habit, Record
from .serializers import HabitSerializer, RecordSerializer


# Create your views here.
class HabitListView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitDetailView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

class RecordListView(ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

class RecordDetailView(RetrieveAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer