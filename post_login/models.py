from django.db import models

# Create your models here.
class Questions(models.Model):
    question = models.CharField(max_length=100)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)

# from django.db import models
# from django.contrib.auth.models import User
# from django.contrib import admin

# #######################
# #Quiz Structure Models#
# #######################

# class Quiz(models.Model):
#     name = models.CharField(max_length = 255)
#     creation = models.DateField(auto_now_add=True)
#     creator = models.ForeignKey(User)

#     def __unicode__ (self):
#         return self.name

#     def possible(self):
#         total = 0
#         for question in self.question_set.all():
#             question.save()
#             total += question.value
#         return total



# class Question(models.Model):
#     question = models.CharField(max_length = 255)
#     quiz = models.ForeignKey(Quiz)
#     creator = models.ForeignKey(User)
#     creation = models.DateField(auto_now_add = True)
#     #objective = TODO: include standards linking in later versions
#     value = models.IntegerField(default = 1)

#     def __unicode__(self):
#         return self.question

# class Answer(models.Model):
#     answer = models.CharField(max_length = 255)
#     question = models.ForeignKey(Question)
#     is_correct = models.BooleanField(default = False)
#     #Creator is tied to the quiz


# ##########
# #Attempts#
# ##########
# class QuizAttempt(models.Model):
#     student = models.ForeignKey(User)
#     quiz = models.ForeignKey(Quiz)
#     date = models.DateField(auto_now_add = True)
#     #Score Method (similar to possible in Quiz 


# class QuestionAttempt(models.Model):
#     attempt = models.ForeignKey(QuizAttempt)
#     question = models.ForeignKey(Question)
#     response = models.ForeignKey(Answer)


# #######
# #Admin#
# #######

# class QuestionInline(admin.StackedInline):
#     model = Question
#     extra = 2


# class AnswerInline(admin.StackedInline):
#     model = Answer
#     extra = 2


# class QuizAdmin(admin.ModelAdmin):
#     list_display = ('name', 'creator', 'creation', 'possible',)
#     search_fields = ('name', 'creator')
#     inlines = [QuestionInline]

# admin.site.register(Quiz, QuizAdmin)

# class QuestionAdmin(admin.ModelAdmin):
#     inlines = [AnswerInline]
#     search_fields = ('question', 'quiz', 'value',)
#     list_display = ('question', 'quiz', 'value',)

# admin.site.register(Question, QuestionAdmin)
