from django.shortcuts import render
from .forms import QuestionForm
from .models import Questions
from django.http import HttpResponseRedirect
# Create your views here.
def quiz(request):
    return render(request,'quizes/quiz.html')

# def question(request):
#     return render(request,'quizes/question.html')

def ques1(request):
    # if request.cmethod == "GET":
        # form = QuestionForm(request.GET)
        # if form.is_valid():
    data = Questions.objects.all();
    dictionary = {
        "obj": data 
    }
            # if obj:
            #     print(obj.answer)
            # detail_item = form.save(commit="False")
            # detail_item.save()
    # else:
        # form = QuestionForm()   
    # cont = {'form':form}
    return render(request,'quizes/ques1.html',dictionary)

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

# def render_quiz(request, quiz_id):
#     quiz = get_object_or_404(Quiz, quiz_id)
#     form = QuizForm(questions=quiz.question_set.all())
#     if request.method == "POST":
#         form = QuizForm(request.POST, questions=quiz.question_set.all())
#         if form.is_valid(): ## Will only ensure the option exists, not correctness.
#             attempt = form.save()
#             return redirect(attempt)
#     return render_to_response('quiz1.html', {"form": form})


