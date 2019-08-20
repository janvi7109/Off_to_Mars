from django.shortcuts import render
from .forms import RegistrationForm
# from .forms import RegistrationForm
# Create your views here.
def home(request):
    return render(request,'page/login.html')

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            detail_item = form.save(commit="False")
            detail_item.save()
    else:
        form = RegistrationForm()   
    cont = {'form':form}
    return render(request,'page/registration.html',cont)
   
# def showform(request):
#     form= BlogCommentsForm(request.POST or None)
#     if form.is_valid():
#         form.save()
  
#     context= {'form': form }
        
#     return render(request, 'Blog/tvreview.html', context)


