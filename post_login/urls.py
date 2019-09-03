from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$', views.quiz , name="quiz"),
    # url(r'^quiz1.html$', views.render_quiz , name="quiz1"),
    url(r'^ques1.html$', views.ques1 , name="ques1"),
    url(r'^ques2.html$', views.ques2 , name="ques2"),
    url(r'^ques3.html$', views.ques3 , name="ques3"),
    url(r'^ques4.html$', views.ques4 , name="ques4"),
    url(r'^score.html$',views.display_function, name="score"),
    url(r'^profile.html$',views.profile,name="profile"),
    url(r'^LoggedOut.html$',views.loggedOut,name="logout")
    # url(r'^registration.html', views.register, name="registration"),
]