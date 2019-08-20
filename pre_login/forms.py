from django import forms
from django.db import models
from .models import Personal_Details

class DesignForm(models.Model):
    username = models.CharField(max_length = 100)
    Email = models.EmailField(primary_key=True,unique=True)
    Age = models.IntegerField(default=19,null=False)
    City = models.CharField(max_length = 50,default="Bangalore")
    State = models.CharField(max_length = 50)
    Country = models.CharField(max_length = 30,default="India")
    Occupation = models.CharField(max_length = 30)
    Password = models.CharField(max_length = 50)


class RegistrationForm(forms.ModelForm):
    Personal_Details.username = forms.TextInput(attrs={'placeholder':"Username"})
    class Meta:
        model = Personal_Details
        # username = forms.CharField("abc")
        fields= ["username","Email","Age","City","State","Country","Occupation","Password"]#,"confirm password"]