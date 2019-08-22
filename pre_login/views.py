from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.core.urlresolvers import reverse_lazy
from .models import Registration
# Create your views here.
def home(request):
    return render(request,'page/login.html')

def register(request):
    return render(request,'page/registration.html')

# class IndexView(generic.ListView):
#     # name of the object to be used in the index.html
#     context_object_name = 'data_list'
#     template_name = 'page/registration.html'
 
#     def get_queryset(self):
#         return Registration.objects.all()


# class UserEntry(CreateView):
#     model = Registration 
#     fields = ['name', 'email']





