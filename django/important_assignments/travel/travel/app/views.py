from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, "index.html")

def register_user(request):
    errors = User.objects.validator_registration(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        print(pw_hash)
        User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            # alias = request.POST['alias'],
            email = request.POST['email'],
            password = pw_hash
        )
        user = User.objects.get(email = request.POST['email'])
        request.session['user_id'] = user.id
        request.session['user_email'] = user.email
        request.session['greeting'] = user.first_name
        # messages.info(request, "User registered; log in now")
        return redirect('/main')

def login_user(request):


    if request.method =='GET':
        return redirect('/')

    errors = User.objects.validator_login(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.get(email = request.POST['email'])
        request.session['user_id'] = user.id
        request.session['user_email'] = user.email
        request.session['greeting'] = user.first_name
        
        return redirect('/main')

def logout(request):
    del request.session['user_id']
    del request.session['user_email']
    return redirect('/')



def main(request):
    if 'user_id' not in request.session:
        messages.error(request, "You are logged out")
        return redirect('/')

    else:
        current_user = User.objects.get(id= request.session['user_id'])
        context={
            'current_user': current_user,
            # 'user_plans': User.objects.user_trip_groups, #. all(),
            'user_plans': Trip.objects.filter(user = current_user),

            'all_trips': Trip.objects.all()
        }
        return render(request,'main.html')
