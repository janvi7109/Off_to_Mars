from django.shortcuts import render
from .forms import QuestionForm
from .models import Questions
from pre_login.forms import LoginForm
from pre_login.forms import RegistrationForm
from pre_login.models import Personal_Details
from django.http import HttpResponseRedirect
from django.utils.datastructures import MultiValueDictKeyError
import time
score = [0, 0, 0, 0]
count = [0, 0, 0, 0]
x = []
start = [0]
stop = [0]
def quiz(request):

    check = {"user":request.session['username']}
    return render(request,'quizes/quiz.html',check)
def question(request):
    return render(request,'quizes/question.html')
def ques1(request):
    data = Questions.objects.all()
    dictionary = {
        "obj": data 
    }
    if request.method == "POST":
        form = QuestionForm(request.POST)
        x.append(time.time())
        try:
            if(request.POST['radio']==data[0].answer):
                if score[0]<1:
                    score[0] += 1
                    count[0]+=1
            else:
                if count[0]>=1 and score[0]==1:
                    score[0]-=1
            return HttpResponseRedirect("ques2.html")
        except MultiValueDictKeyError:
            return HttpResponseRedirect("ques2.html")
    else:
        form = QuestionForm()
    cont = {'form':form}
    return render(request,'quizes/ques1.html',dictionary,cont)



def ques2(request):
    data = Questions.objects.all()
    dictionary = {
        "obj": data 
    }
    if request.method == "POST":
        form = QuestionForm(request.POST)
        try:
            if(request.POST['radio']==data[1].answer):
                if score[1]<1:
                    score[1] += 1
                    count[1]+=1
            else:
                if count[1]>=1 and score[1]==1:
                    score[1]-=1
            return HttpResponseRedirect("ques3.html")
        except MultiValueDictKeyError:
            return HttpResponseRedirect("ques3.html")
    else:
        form = QuestionForm()
    cont = {'form':form}
    return render(request,'quizes/ques2.html',dictionary,cont)

def ques3(request):
    data = Questions.objects.all()
    dictionary = {
        "obj": data 
    }
    if request.method == "POST":
        form = QuestionForm(request.POST)
        try:
            if(request.POST['radio']==data[2].answer):
                if score[2]<1:
                    score[2] += 1
                    count[2] +=1
            else:
                if count[2]>=1 and score[2]==1:
                    score[2]-=1
            return HttpResponseRedirect("ques4.html")
        except MultiValueDictKeyError:
            return HttpResponseRedirect("ques4.html")
    else:
        form = QuestionForm()
    cont = {'form':form}
    return render(request,'quizes/ques3.html',dictionary,cont)

def ques4(request):
    data = Questions.objects.all()
    dictionary = {
        "obj": data 
    }
    if request.method == "POST":
        form = QuestionForm(request.POST)
        try:
            if(request.POST['radio']==data[3].answer):
                if score[3]<1:
                    score[3] += 1
                    count[3] += 1
            else:
                if count[3]>=1 and score[3]==1:
                    score[3]-=1
            start[0] = x[0]
            stop[0] = time.time()
            request.session['time'] = stop[0]-start[0]
            print(request.session['time'])
            return HttpResponseRedirect("score.html")
        except MultiValueDictKeyError:
            return HttpResponseRedirect("score.html")
    else:
        form = QuestionForm()
    cont = {'form':form}
    return render(request,'quizes/ques4.html',dictionary,cont)

def display_function(request):
    
    result = 0
    for i in score:
        result += i
    request.session['score'] = result
    print(result)
    return render(request,'quizes/score.html',{"result":request.session['score'], "time": request.session['time']})

def profile(request):
    info = Personal_Details.objects.get(Email=request.session['Email'])
    details = {"score" : request.session['score'], "time": request.session['time'], "username" : info.username, "Age" : info.Age, "City":
    info.City, "State": info.State, "Country" : info.Country, "Occupation" : info.Occupation}
    return render(request,'quizes/profile.html', details)