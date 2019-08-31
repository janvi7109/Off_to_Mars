from django.shortcuts import render
from .forms import RegistrationForm
from .forms import LoginForm
from .models import Personal_Details
from django.http import HttpResponseRedirect
from django.contrib import messages
# from .forms import RegistrationForm
# Create your views here.
def home(request):
    return render(request,'page/login.html')

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            detail_item = form.save(commit="False")
            detail_item.save()
            form = LoginForm()
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()   
    cont = {'form':form}
    return render(request,'page/registration.html',cont)

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST) 
        if form.is_valid():
            print("hi")
            input_data = form.cleaned_data
            try:
                obj = Personal_Details.objects.get(Email=input_data['Email'])
                if(obj.Password == input_data['Password']):
                    user = {"user":obj.username}
                    return render(request,'quizes/quiz.html',user)
            except:
                print("Unidentified User")
    else:
        form = LoginForm()
    cont = {'form':form}
    return render(request,'page/login.html',cont)
