from django.shortcuts import render, redirect
from  .models import *
from django.contrib import messages

# Create your views here.

def landing(request):
    return render(request, 'landing.html')

def login_user(request):

    errors = User.objects.login_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/login')

    user = User.objects.get(email = request.POST['email'])
    request.session['user_id'] = user.id
    request.session['greeting'] = user.first_name

    return redirect('/dashboard')


def login(request):
    return render(request, 'login.html')

def register(request):
    # errors = User.objects.basic_validator(request.POST)
    # if len(errors)>0:
    #     for key, value in errors.items():
    #         messages.error(request, value)
    #     return redirect('/register')
    return render(request, 'register.html')

def register_user(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/register')


    user = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password= bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()  
    )
    request.session['user_id'] = user.id
    request.session['greeting'] = user.first_name


    print("Useeeeeer IDDDDD", user.id)
    if user.id == 1:
        print("this user is admin")
    
    return redirect('/dashboard')

def dashboard(request):

    users = User.objects.all()
    context= {
        'users': users
    }
    return render(request, 'dashboard.html', context)


def show_user(request, user_id):
    user= User.objects.get(id =user_id)
    context={
        "user": user
    }

    return render(request, 'show_user.html', context)

def submit_message(request, user_id):
    print( "Userrrrrrrr", user_id)

    user = User.objects.get(id=request.session["user_id"])
    new_post = Message.objects.create(
        post = request.POST['post'],
        poster=user 
        )


    return redirect(f'/users/show/{user.id}')


def admin_delte_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('/dashboard')