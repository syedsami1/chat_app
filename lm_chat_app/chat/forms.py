# chat/forms.py
from django import forms

class ChatForm(forms.Form):
    message = forms.CharField(label='Your message', max_length=100)
    model = forms.ChoiceField(label='Select model', choices=[
        ('gpt2', 'GPT-2'),
        ('distilgpt2', 'DistilGPT-2'),
        # Add more models as needed
    ])
