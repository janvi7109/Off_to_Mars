from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'page/login.html')

def register(request):
    return render(request,'page/registration.html')