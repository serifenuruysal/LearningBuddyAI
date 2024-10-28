# conversations/models.py
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    language_preference = models.CharField(max_length=50, default='English')
    tone_preference = models.CharField(max_length=50, choices=[('formal', 'Formal'), ('informal', 'Informal')], default='informal')

class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_input = models.TextField()
    ai_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class ConversationHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    messages = models.JSONField()  # Store messages as a JSON array
