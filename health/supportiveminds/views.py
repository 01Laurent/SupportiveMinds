from django.shortcuts import render, redirect
from .models import MoodEntry, ChatMessage
import openai

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def mood_tracker(request):
    if request.method == 'POST':
        mood = request.POST['mood']
        note = request.POST['note']
        MoodEntry.objects.create(user=request.user, mood=mood, note=note)
        return redirect('support:mood_tracker')

    return render(request, 'mood_tracker.html')

def resources(request):
    return render(request, 'resources.html')

openai.api_key = 'your-openai-api-key'
def chat_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=150
        )
        bot_response = response.choices[0].text.strip()
        return render(request, 'chat.html', {'bot_response': bot_response})

    return render(request, 'chat.html')

def get_ai_response(user_message):
    response = openai.Completion.create(
        model=ChatMessage,
        prompt=user_message,
        max_tokens=150
    )
    return response.choices[0].text.strip()