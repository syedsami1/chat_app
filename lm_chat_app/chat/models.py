from django.db import models

class Conversation(models.Model):
    user = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    text = models.TextField()
    is_user = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
