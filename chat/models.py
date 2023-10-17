# chat/models.py
from django.db import models

class Message(models.Model):
    sender = models.CharField(max_length=50)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
