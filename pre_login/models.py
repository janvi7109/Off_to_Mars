# from django.contrib.auth import authenticate, login
from django.db import models
# from django.contrib.auth.models import User
from django import forms
# forms.Select(widget=forms.Select)

class Personal_Details(models.Model):
    username = models.CharField(max_length = 100)
    Email = models.EmailField(primary_key=True,unique=True)
    Age = models.IntegerField(default=19,null=False)
    City = models.CharField(max_length = 50,default="Bangalore")
    State = models.CharField(max_length = 50)
    Country = models.CharField(max_length = 30,default="India")
    Occupation = models.CharField(max_length = 30)
    Password = models.CharField(max_length = 50)
    '''widget=forms.PasswordInput(),null=False)'''

# def my_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
        
#     else:
#         print("Invalid Credentials!!")


        