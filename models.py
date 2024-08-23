# models.py
from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscription_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    responded = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}"
