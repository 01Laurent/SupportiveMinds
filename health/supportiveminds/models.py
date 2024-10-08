from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    favorite_coping_mechanism = models.CharField(max_length=255, blank=True)
    preferred_support_type = models.CharField(max_length=100, choices=[
        ('online', 'Online Support'),
        ('in_person', 'In-Person Support'),
        ('anonymous', 'Anonymous Support')
    ], default='online')

    def __str__(self):
        return f'{self.user.username} Profile'

class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=50)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Tag(models.Model):
    name = models.CharField(max_length=50)

class MentalHealthResource(models.Model):
    RESOURCE_TYPES = [
        ('article', 'Article'),
        ('video', 'Video'),
        ('podcast', 'Podcast'),
        ('infographic', 'Infographic'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=255)
    resource_link = models.URLField(max_length=200)
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPES)
    resource_description = models.TextField()
    summary = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)
    is_private = models.BooleanField(default=False)
    file_upload = models.FileField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return self.title