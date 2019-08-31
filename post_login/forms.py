from django import forms
from django.db import models
from .models import Questions

# class DesignForm(models.Model):
#     username = models.CharField(max_length = 100)
#     Email = models.EmailField(primary_key=True,unique=True)
#     Age = models.IntegerField(default=19,null=False)
#     City = models.CharField(max_length = 50,default="Bangalore")
#     State = models.CharField(max_length = 50)
#     Country = models.CharField(max_length = 30,default="India")
#     Occupation = models.CharField(max_length = 30)
#     Password = models.CharField(max_length = 50)


class QuestionForm(forms.ModelForm):
    # question = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Question'}))
    # Email = forms.EmailField(label='',widget=forms.TextInput(attrs={'placeholder':'Email'}))
    # Age = forms.IntegerField(label='',widget=forms.TextInput(attrs={'placeholder':'Age'}))
    # City = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'City'}))
    # State = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'State'}))
    # Country = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Country'}))
    # Occupation = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Occupation'}))
    # Password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    class Meta:
        model = Questions
        # username = forms.CharField("abc")
        fields = ["question","option1","option2","option3","option4","answer"]#,"Occupation","Password"]#,"confirm password"]
    # def __init__(self, data, questions, *args, **kwargs):
    #     self.questions = questions
    #     for question in questions:
    #         field_name = "question_%d" % question.pk
    #         choices = []
    #         for answer in question.answer_set().all():
    #             choices.append((answer.pk, answer.answer,))
    #         ## May need to pass some initial data, etc:
    #         field = forms.ChoiceField(label=question.question, required=True, 
    #                                   choices=choices, widget=forms.RadioSelect)
    #     return super(QuizForm, self).__init__(data, *args, **kwargs)
    # def save(self):
