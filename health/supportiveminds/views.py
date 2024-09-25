from django.shortcuts import render, redirect
from .models import MoodEntry, MentalHealthResource, Profile
import openai
import os
from dotenv import load_dotenv
from django.http import JsonResponse
from .forms import MentalHealthResourceForm, CustomUserCreationForm

load_dotenv()
openai.api_key = ''

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a corresponding profile for the user
            Profile.objects.create(
                user=user,
                date_of_birth=form.cleaned_data.get('date_of_birth'),
                phone_number=form.cleaned_data.get('phone_number'),
                favorite_coping_mechanism=form.cleaned_data.get('favorite_coping_mechanism'),
                preferred_support_type=form.cleaned_data.get('preferred_support_type')
            )
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

# Create your views here.
def home_view(request):
    # Check if the request is a POST request
    if request.method == 'POST':
        user_message = request.POST.get('message')
        print("User message:", user_message)  # Check if the message is received correctly

        try:
            # Uncomment the following lines to use the OpenAI API
            # response = openai.ChatCompletion.create(
            #     model="gpt-3.5-turbo",
            #     messages=[
            #         {"role": "system", "content": "You are a helpful assistant."},
            #         {"role": "user", "content": user_message}
            #     ]
            # )

            # ai_response = response.choices[0].message["content"]
            ai_response = "This is a placeholder response. The OpenAI API quota has been exceeded."
            print("AI response:", ai_response)  # Check if OpenAI responded correctly

            return JsonResponse({'response': ai_response})
        except Exception as e:
            print("Error occurred:", str(e))  # Output the error
            return JsonResponse({'error': 'Something went wrong.'}, status=500)

    # If it's a GET request, render the home page with resources
    resources = MentalHealthResource.objects.all().order_by('-created_at')
    
    context = {
        'resources': resources,
    }
    return render(request, 'home.html', context)

def mood_tracker(request):
    if request.method == 'POST':
        mood = request.POST['mood']
        note = request.POST['note']
        MoodEntry.objects.create(user=request.user, mood=mood, note=note)
        return redirect('support:mood_tracker')

    return render(request, 'mood_tracker.html')

def resources(request):
    return render(request, 'resources.html')

def resources_view(request):
    resources = MentalHealthResource.objects.all().order_by('-created_at')
    
    if request.method == 'POST':
        form = MentalHealthResourceForm(request.POST, request.FILES)  # Include files
        if form.is_valid():
            resource = form.save(commit=False)
            resource.user = request.user  # Associate the resource with the logged-in user
            resource.save()
            return redirect('ideas')  # Redirect after successful submission
    else:
        form = MentalHealthResourceForm()
    
    context = {
        'resources': resources,
        'form': form,
    }
    return render(request, 'share_ideas.html', context)



