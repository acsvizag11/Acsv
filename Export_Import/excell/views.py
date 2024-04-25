from django.shortcuts import render,HttpResponseRedirect
from .models import home
from .forms import Studentregi
from django.contrib.auth import authenticate

# Create your views here.

def Student(request):
    if request.method=="POST":
        fm=Studentregi(request.POST)
        if fm.is_valid():
            S_no=fm.cleaned_data['s_no']
            First_Name=fm.cleaned_data['first_name']
            Last_Name=fm.cleaned_data['last_name']
            Email=fm.cleaned_data['email']
            reg=home(s_no=S_no,First_Name=First_Name,last_name=Last_Name,email=Email)
            reg.save()

        return HttpResponseRedirect('/profile/')
        
    else:
        fm=Studentregi()
        stud=home.objects.all()
    return render(request, 'Userlogin.html',{'form':fm},{'stu':stud})
