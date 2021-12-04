from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Habit(models.Model):
        user = models.ForeignKey(
            'User', on_delete=models.CASCADE, default=None,)
        name = models.CharField(max_length=100)
        goal = models.IntegerField()
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.name

        def __repr__(self):
            return f"<Habit name={self.name}>"

class Record(models.Model):
    habit = models.ForeignKey(
            'Habit', on_delete=models.CASCADE, default=None,)
    amount = models.IntegerField()
    date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

# when these aren't commented out throws error at add_record in admin
    def __str__(self):
        return self.amount

    def __repr__(self):
        return f"<Record name={self.amount}>"

