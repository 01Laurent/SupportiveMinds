from django import forms
from .models import MentalHealthResource

class MentalHealthResourceForm(forms.ModelForm):
    class Meta:
        model = MentalHealthResource
        fields = ['title', 'resource_link', 'resource_type', 'resource_description', 'summary', 'tags', 'file_upload']