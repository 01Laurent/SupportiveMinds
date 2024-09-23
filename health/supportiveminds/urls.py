from django.urls import path
from .views import home_view, resources, chat_view, mood_tracker

urlpatterns = [
    path('', home_view, name='home'),
    path('resources/', resources, name='resources'),
    path('mood_tracker/', mood_tracker, name='mood_tracker'),
    path('chat/', chat_view, name='chat'),


]