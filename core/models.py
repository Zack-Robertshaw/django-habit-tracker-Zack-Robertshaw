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
        name = models.TextField()
        goal = models.IntegerField()
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.title

        def __repr__(self):
            return f"<Habit name={self.title}>"

class Record(models.Model):
    habit_id = models.ForeignKey(
            'Habit', on_delete=models.CASCADE, default=None,)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<Record name={self.title}>"


