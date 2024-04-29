from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai

from .models import Chat
from users.models import CustomUser


import os
from openai import OpenAI
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from dotenv import load_dotenv




load_dotenv()

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

def ask_openai(message):
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": message,
        }
    ],
    model="gpt-3.5-turbo-0125",
)
    
    answer = chat_completion.choices[0].message.content.strip()
    return answer


#@login_required(login_url='users:login')
def chatbot(request):
    user_id = request.session.get('user_id')
    if not user_id:
        # Handle case where user_id is not in session
        return JsonResponse({'error': 'User ID not found in session'}, status=400)
    
    try:
        chats = Chat.objects.filter(user_id=user_id)
    except ValueError:
        # Handle case where user_id is not a valid integer
        return JsonResponse({'error': 'Invalid User ID'}, status=400)
    print(user_id)
    
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        # Save the chat with the logged-in user
        chat = Chat(user_id=user_id, message=message, response=response, created_at=timezone.now())
        chat.save()

        return JsonResponse({'message': message, 'response': response})
    
    return render(request, 'chatbot.html', {'chats': chats})