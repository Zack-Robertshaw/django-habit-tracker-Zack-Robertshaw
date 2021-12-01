from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Habit, Record
from .forms import HabitForm, RecordForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    user = request.user
    decks = Habit.objects.filter(user=user.pk)

    return render(request, "tracker/home.html", {
        "user": user,})
# # "habits": habits,   will be needed eventually.  Don't forget to put it back in.
#         "user": user, "habits": habits,})

#this shows all habits at homepage
def show_habit(request, pk):
    pass



#make a new habit w/ form
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
            # Should ideally redirect to add card
            return redirect(to='home')

    return render(request, "tracker/add_habit.html", {
        "user": user, "form": form, })



# #edit, update, record habit, show progress on this page
# def edit_habit(request, pk):
#     pass



# #button on homepage habit for delete
# def delete_habit(request,pk):
#     pass
