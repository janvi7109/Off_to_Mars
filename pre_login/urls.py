from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$', views.login, name="login"),
    url(r'^registration.html', views.register, name="registration"),
    # url(r'^quiz.html$', views.quiz , name="quiz"),
    # url(r'^question.html$', views.question , name="question"),
    # url(r'^ques1.html$', views.ques1 , name="ques1"),
]