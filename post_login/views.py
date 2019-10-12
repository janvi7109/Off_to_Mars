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
p = [-1]
start = [0]
stop = [0]
def quiz(request):
    if 'Email' not in request.session:
        return HttpResponseRedirect("/quiz/LoggedOut.html")
    obj = Personal_Details.objects.get(Email=request.session['Email'])
    check = {"user":obj.username,"time_taken":obj.Time}
    if request.method == "POST":
        print('Hi')
        print(request.session['time'])
        if(request.session['time'] == 0):
            return HttpResponseRedirect("/quiz/ques1.html")
    return render(request,'quizes/quiz.html',check)

# def ques(request):
#     x.append(time.time())
#     if request.method == "POST":
#         form = QuestionForm(request.POST)
    

def ques1(request):
    if 'Email' not in request.session:
        return HttpResponseRedirect("/quiz/LoggedOut.html")
    data = Questions.objects.all()
    dictionary = {
        "obj": data 
    }
    if request.method == "POST":
        form = QuestionForm(request.POST)
        x.append(time.time())
        p[0] += 1
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
    if 'Email' not in request.session:
        return HttpResponseRedirect("/quiz/LoggedOut.html")
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
    if 'Email' not in request.session:
        return HttpResponseRedirect("/quiz/LoggedOut.html")
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
    if 'Email' not in request.session:
        return HttpResponseRedirect("/quiz/LoggedOut.html")
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
            start[0] = x[p[0]]
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
    if 'Email' not in request.session:
        return HttpResponseRedirect("/quiz/LoggedOut.html")
    result = 0
    for i in score:
        result += i
    request.session['score'] = result
    print(start[0],stop[0])
    Personal_Details.objects.filter(Email=request.session['Email']).update(Time=request.session['time'])
    Personal_Details.objects.filter(Email=request.session['Email']).update(Score=request.session['score'])    
    print(result)
    print(request.session['time'])
    return render(request,'quizes/score.html',{"result":request.session['score'], "time": request.session['time']})

def profile(request):
    if 'Email' not in request.session:
        return HttpResponseRedirect("/quiz/LoggedOut.html")
    info = Personal_Details.objects.get(Email=request.session['Email'])
    details = {"score" : info.Score, "time": info.Time, "username" : info.username, "Age" : info.Age, "City":
    info.City, "State": info.State, "Country" : info.Country, "Occupation" : info.Occupation}
    return render(request,'quizes/profile.html', details)

def loggedOut(request):
    try:
        obj =  Personal_Details.objects.get(Email=request.session['Email'])
        back = {"user":obj.username+"."}
        del request.session['Email']
        del request.session['time']
        del request.session['score']
    except KeyError:
        back = {"user":""}
        pass
    return render(request,'quizes/LoggedOut.html',back)