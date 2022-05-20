from tkinter import CASCADE
from django.db import models
from users.models import User

class Item(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    amount = models.PositiveIntegerField()
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'name': self.name,
            'color': self.color,
            'amount': self.amount,
            'user': self.user.id
        }
