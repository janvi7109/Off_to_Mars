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
            print(form.cleaned_data)
            print(form.cleaned_data['Email'])
            obj = Personal_Details.objects.get(Email=form.cleaned_data['Email'])
            # #  = Personal_Details.objects.get(Email=form.cleaned_data['Email'])
            if(obj):
                if(form.cleaned_data['Password']==obj.Password):
                    return HttpResponseRedirect("quiz.html")
    else:
        form = LoginForm()
    cont = {'form':form}
    return render(request,'page/login.html',cont)

# def showform(request):
#     form= BlogCommentsForm(request.POST or None)
#     if form.is_valid():
#         form.save()
  
#     context= {'form': form }
        
#     return render(request, 'Blog/tvreview.html', context)
# def quiz(request):
#     return render(request,'quizes/quiz.html')

# def question(request):
#     return render(request,'quizes/question.html')

# def ques1(request):
#     return render(request,'quizes/ques1.html')


