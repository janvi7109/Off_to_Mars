from django.shortcuts import render
from .forms import RegistrationForm
from .forms import LoginForm
from .models import Personal_Details
from django.http import HttpResponseRedirect
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
    else:
        form = RegistrationForm()   
    cont = {'form':form}
    return render(request,'page/registration.html',cont)

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST) 
        if form.is_valid():
            print("hi")
            print(form.cleaned_data)
            obj = Personal_Details.objects.get(Email=form.cleaned_data['Email'])
            if(obj):
                print(obj.Age)
                return HttpResponseRedirect("registration.html")
            else:
                print("Didn't happen")
    else:
        form = LoginForm()
    cont = {'form':form}
    return render(request,'page/login.html',cont)
