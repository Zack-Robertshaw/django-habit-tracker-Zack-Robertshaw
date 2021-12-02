from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Habit, Record
from .forms import HabitForm, RecordForm
from django.contrib.auth.decorators import login_required


def home(request):
    user = request.user
    habits = Habit.objects.filter(user=user.pk)

    return render(request, "tracker/home.html", {
        "user": user, "habits": habits,})




@login_required
def add_habit(request):
    user = request.user
    if request.method == 'GET':
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user_id = user.pk
            habit.save()
            return redirect(to='home')

    return render(request, "tracker/add_habit.html", {
        "user": user, "form": form, })



@login_required
def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        habit.delete()
        return redirect(to='/')
    return render(request, "tracker/delete_habit.html",
                  {"habit": habit})


# #edit, update, record habit, show progress on this page
# def edit_habit(request, pk):
#     pass
