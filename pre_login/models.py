# from django.contrib.auth import authenticate, login

# def my_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
        
#     else:
#         print("Invalid Credentials!!")


from django.db import models

class Registration(models.Model):
    name= models.CharField(max_length=15)
    email= models.EmailField()
    # age= models.CharField(max_length=10000)
      