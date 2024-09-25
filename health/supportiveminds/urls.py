from django.urls import path
from .views import home_view, resources, mood_tracker, resources_view

urlpatterns = [
    path('', home_view, name='home'),
    path('resources/', resources, name='resources'),
    path('mood_tracker/', mood_tracker, name='mood_tracker'),
    path('ideas/', resources_view, name='ideas' ),
]