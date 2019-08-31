from django import forms
from django.db import models
from .models import Questions
from django.forms.widgets import RadioSelect

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ["question","option1","option2","option3","option4","answer"]
        Radio_Choices = ["option1", "option2", "option3", "option4"]
        radio = forms.ChoiceField( widget=RadioSelect(), choices=Radio_Choices)


        