from django.contrib import admin
from .models import MoodEntry, ChatMessage

# Register your models here.
admin.site.register(MoodEntry)
admin.site.register(ChatMessage)
