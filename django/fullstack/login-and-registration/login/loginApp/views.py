from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')



def register(request):
    if request.method=="GET":
        return redirect('/')
    else:

        errors = User.objects.validator(request.POST)
        if len(errors)>0:
            for key,val in errors.items():
                messages.error(request, val)
            return redirect('/')

        else:
            if request.POST["password"] == request.POST["confirm_password"]:
                User.objects.create(
                    first_name= request.POST["first_name"],
                    last_name= request.POST["last_name"],
                    email= request.POST["email"],
                    password= request.POST["password"],
                )
            else:
                print("passwords don't match")
                return redirect('/')
    return redirect('/')

