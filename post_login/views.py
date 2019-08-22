from django.shortcuts import render

# Create your views here.



# Create your views here.
def quiz(request):
    return render(request,'quizes/quiz.html')

def question(request):
    return render(request,'quizes/question.html')

def ques1(request):
    return render(request,'quizes/ques1.html')