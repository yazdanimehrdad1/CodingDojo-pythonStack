from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def register(request):

    errors = User.objects.validator_registration(request.POST)

    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        new_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        )
        request.session["user_id"] = new_user.id
        request.session["greeting"] =  f'{new_user.first_name}  {new_user.last_name}'
        return redirect('/wall')


def login(request):
    errors= User.objects.validator_login(request.POST)

    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.get(email = request.POST['email'])
        request.session["user_id"] = user.id
        request.session["greeting"] = f'{user.first_name}  {user.last_name}'

        return redirect('/wall')

def create_message(request):
    Message.objects.create(
        message= request.POST['message'],
        message_created_by = User.objects.get(id= request.session["user_id"])
    )
    print(Message.message)

    return redirect('/wall')

def create_comment(request, message_id):
    message = Message.objects.get(id=message_id)
    user = User.objects.get(id= request.session["user_id"])
    created_comment = Comment.objects.create(
        comment = request.POST['comment'],
        comment_created_by=user,
        comment_of_message = message
    )
    return redirect('/wall')


def logout(request):
    request.session.flush()
    return redirect('/')

def main(request):
    # handle errors

    
    return render(request, 'login.html')

def wall(request):
    users = User.objects.all()
    messages= Message.objects.all()
    
    context={
        "users":users,
        "messages":messages

    }
    return render(request, 'main.html',context)

