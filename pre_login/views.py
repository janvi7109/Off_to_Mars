from django.shortcuts import render
from .forms import RegistrationForm
# Create your views here.
def home(request):
    return render(request,'page/login.html')

def register(request):
    return render(request,'page/registration.html')

def showform(request):
    form= BlogCommentsForm(request.POST or None)
    if form.is_valid():
        form.save()
  
    context= {'form': form }
        
    return render(request, 'Blog/tvreview.html', context)


