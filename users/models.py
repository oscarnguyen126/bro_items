from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return self.email

    def to_dict(self):
        return {
            'email': self.email,
            'username': self.username,
            'password': self.password,
        }
