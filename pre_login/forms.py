from django import forms
from django.db import models
from .models import Personal_Details

# class DesignForm(models.Model):
#     username = models.CharField(max_length = 100)
#     Email = models.EmailField(primary_key=True,unique=True)
#     Age = models.IntegerField(default=19,null=False)
#     City = models.CharField(max_length = 50,default="Bangalore")
#     State = models.CharField(max_length = 50)
#     Country = models.CharField(max_length = 30,default="India")
#     Occupation = models.CharField(max_length = 30)
#     Password = models.CharField(max_length = 50)


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Username'}))
    Email = forms.EmailField(label='',widget=forms.TextInput(attrs={'placeholder':'Email'}))
    Age = forms.IntegerField(label='',widget=forms.TextInput(attrs={'placeholder':'Age'}))
    City = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'City'}))
    State = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'State'}))
    Country = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Country'}))
    Occupation = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Occupation'}))
    Password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    class Meta:
        model = Personal_Details
        # username = forms.CharField("abc")
        fields = ["username","Email","Age","City","State","Country","Occupation","Password"]#,"confirm password"]

class LoginForm(forms.Form):
    Email = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Email'}))
    Password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    class Meta:
        fields = ["username","Password"] 