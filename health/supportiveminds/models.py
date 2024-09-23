from django.db import models
from django.contrib.auth.models import User

class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=50)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class ChatMessage(models.Model):
    session_id = models.CharField(max_length=255)  # Anonymous sessions tracked by session ID
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)