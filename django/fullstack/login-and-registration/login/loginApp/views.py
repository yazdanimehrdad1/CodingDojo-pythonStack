from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')



def register(request):
    if request.method=="GET":
        return redirect('/')
    
    errors = User.objects.validator(request.POST)
    if len(errors)>0:
        for key,val in errors.items():
            messages.error(request, val)
        return redirect('/')

    else:
        new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id
        messages.success(request, "you have successfuly registered!")
        return redirect('/success')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')

    user = User.objects.get(id= request.session['user_id'])
    context={
        'user':user
    }
    return render(request,'success.html',context )

def logout(request):
    request.session.clear()
    return redirect('/')

def login(request):
    if request.method == "GET":
        return redirect('/')
    
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid Email/password')
        return redirect('/')
    user =User.objects.get(email= request.POST['email'])
    request.session['user_id'] = user.id
    messages.success(request, 'You have successfully logged in')
    return redirect('/success')