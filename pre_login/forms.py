from django import forms
from .models import BlogComments

class RegistrationForm(forms.ModelForm):
    class Meta:
        model= Registration
        fields= ["name", "email"]