from django.shortcuts import render
from .models import User, Habit, Record
# from .forms import 
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    user = request.user
    decks = Habit.objects.filter(user=user.pk)

    return render(request, "tracker/home.html", {
        "user": user,})
# # "habits": habits,   will be needed eventually.  Don't forget to put it back in.
#         "user": user, "habits": habits,})
