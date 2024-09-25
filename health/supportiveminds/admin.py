from django.contrib import admin
from .models import MoodEntry, MentalHealthResource

# Register your models here.
admin.site.register(MoodEntry)
admin.site.register(MentalHealthResource)
