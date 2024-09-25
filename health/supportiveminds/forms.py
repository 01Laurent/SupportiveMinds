from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import MentalHealthResource, Profile

class MentalHealthResourceForm(forms.ModelForm):
    class Meta:
        model = MentalHealthResource
        fields = ['title', 'resource_link', 'resource_type', 'resource_description', 'summary', 'tags', 'file_upload']

class CustomUserCreationForm(UserCreationForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    favorite_coping_mechanism = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    preferred_support_type = forms.ChoiceField(choices=[
        ('online', 'Online Support'),
        ('in_person', 'In-Person Support'),
        ('anonymous', 'Anonymous Support')
    ], required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'date_of_birth', 'phone_number', 'favorite_coping_mechanism', 'preferred_support_type')