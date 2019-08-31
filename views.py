from django.shortcuts import render
from .forms import QuestionForm
from .models import Questions
from django.http import HttpResponseRedirect
# Create your views here.
score = [0, 0, 0, 0]
count = [0, 0, 0, 0]
def quiz(request):
    return render(request,'quizes/quiz.html')

# def question(request):
#     return render(request,'quizes/question.html')

def question(request):
    # if request.method == "GET":
    #     form = QuestionForm(request.GET)
    #     if form.is_valid():
    #         obj = Questions.objects.all();
    #         # if obj:
    #         #     print(obj.answer)
    #         # detail_item = form.save(commit="False")
    #         # detail_item.save()
    # else:
    #     form = QuestionForm()   
    # cont = {'form':form}
    return render(request,'quizes/question.html')

def ques1(request):
    # score = 0
    data = Questions.objects.all()
    dictionary = {
        "obj": data 
    }
    if request.method == "POST":
        print("HELLO")
        form = QuestionForm(request.POST)
        if form.is_valid():
            print("HII")
        for i in request.POST:
            print(i)
        print(request.POST)
        print(data[0].question)
        if(request.POST['radio']==data[0].answer):
            if score[0]<1:
                score[0] += 1
                count[0]+=1
        else:
            if count[0]>=1 and score[0]==1:
                score[0]-=1

        print(score)
        return HttpResponseRedirect("ques2.html")
    else:
        form = QuestionForm()
    cont = {'form':form}
    return render(request,'quizes/ques1.html',dictionary,cont)



def ques2(request):
    # score = 0
    data = Questions.objects.all()
    dictionary = {
        "obj": data 
    }
    if request.method == "POST":
        form = QuestionForm(request.POST)
        # if form.is_valid():
        #     print("HII")
        # for i in request.POST:
        #     print(i)
        # print(request.POST['radio'])
        print(data[1].question)
        if(request.POST['radio']==data[1].answer):
            if score[1]<1:
                score[1] += 1
                count[1]+=1
        else:
            if count[1]>=1 and score[1]==1:
                score[1]-=1

        print(score)
        return HttpResponseRedirect("ques3.html")
        # return ques3(request)
        # return render(request,'quizes/ques3.html',dictionary,{'form':form})
    else:
        form = QuestionForm()
    cont = {'form':form}
    return render(request,'quizes/ques2.html',dictionary,cont)

def ques3(request):
    # score = 0
    data = Questions.objects.all()
    dictionary = {
        "obj": data 
    }
    if request.method == "POST":
        form = QuestionForm(request.POST)
        # if form.is_valid():
        #     print("HII")
        # for i in request.POST:
        #     print(i)
        # print(request.POST['radio'])
        print(data[2].question)
        if(request.POST['radio']==data[2].answer):
            if score[2]<1:
                score[2] += 1
                count[2] +=1
            
        else:
            if count[2]>=1 and score[2]==1:
                score[2]-=1

        print(score)
        return HttpResponseRedirect("ques4.html")
        # return ques4(request)
        # return render(request,'quizes/ques4.html',dictionary,{'form':form})
    else:
        form = QuestionForm()
    cont = {'form':form}
    return render(request,'quizes/ques3.html',dictionary,cont)

def ques4(request):
    # score = 0
    data = Questions.objects.all()
    dictionary = {
        "obj": data 
    }
    if request.method == "POST":
        form = QuestionForm(request.POST)
        # if form.is_valid():
        #     print("HII")
        # for i in request.POST:
        #     print(i)
        # print(request.POST['radio'])
        print(data[3].question)
        if(request.POST['radio']==data[3].answer):
            if score[3]<1:
                score[3] += 1
                count[3] +=1
        else:
            if count[3]>=1 and score[3]==1:
                score[3]-=1
        

        print(score)
        final = score[0]+score[1]+score[2]+score[3]
        print(final)
        # return HttpResponseRedirect("ques4.html")
    else:
        form = QuestionForm()
    cont = {'form':form}
    return render(request,'quizes/ques4.html',dictionary,cont)
