# chat/views.py
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .services import get_language_model
from .models import Conversation, Message
from django.conf import settings

# MongoDB client and database from settings.py
db = settings.db

# Language models dictionary
lm_models = {
    'gpt2': get_language_model('gpt2'),
    'distilgpt2': get_language_model('distilgpt2'),
    # Add more models as needed
}

@csrf_exempt
def chat_view(request):
    if request.method == 'POST':
        user_message = request.POST['message']
        model_name = request.POST['model']

        # Get model and generate response
        lm = lm_models.get(model_name)
        if lm:
            bot_response = lm(user_message, max_length=100)[0]['generated_text']
        else:
            bot_response = "Model not found or configured."

        # Save conversation and messages to MongoDB
        conversation = Conversation.objects.create(user=request.user.username, model_name=model_name)
        Message.objects.create(conversation=conversation, text=user_message, is_user=True)
        Message.objects.create(conversation=conversation, text=bot_response, is_user=False)

        return JsonResponse({
            'user_message': user_message,
            'bot_response': bot_response,
            'model_name': model_name,
        })
    else:
        return render(request, 'chat/chat.html')

def chat_history_view(request):
    # Retrieve all conversations for the current user
    conversations = Conversation.objects.filter(user=request.user.username)

    return render(request, 'chat/history.html', {
        'conversations': conversations,
    })
