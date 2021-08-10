# from django.http.response import HttpResponse
from django.contrib.messages.constants import DEFAULT_LEVELS
from django.shortcuts import redirect, render, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):

    errors = User.objects.validator_registration(request.POST)

    if len(errors):
        for key,value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        )

        request.session['user_id'] = user.id
        request.session['greeting'] = user.first_name
        return redirect('/books')


def login(request):
    errors= User.objects.validator_login(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    user = User.objects.get(email=request.POST['email'])

    request.session['user_id'] = user.id
    request.session['greeting'] = user.first_name
    return redirect('/books')


def show_all(request):
    
    if "user_id" not in request.session:
        return redirect('/')
    else:
        context={
            "all_books": Book.objects.all(),
            "this_user": User.objects.get(id=request.session['user_id'])
        }
        return render(request, 'show_all.html', context)

def create(request):

    errors = Book.objects.validator_book(request.POST)

    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect('/books')

    else:
        user= User.objects.get(id=request.session["user_id"])
        book =Book.objects.create(
            title=request.POST['title'],
            description = request.POST['description'],
            created_by = user
        )
        # user.favorited_books.add(book)
        return redirect(f'/books/{book.id}')

def show_one(request, book_id):
    context={
        'book': Book.objects.get(id=book_id),
        'current_user': User.objects.get(id= request.session['user_id'])
    
    }
    return render(request, 'show_one.html', context)

# update
# favorit
def favorit(request, book_id):


    print("Book_iddddddddddddddd", book_id)
    user = User.objects.get(id=request.session["user_id"])
    book = Book.objects.get(id=book_id)
    user.favorited_books.add(book)
    return redirect('/books')

# unfavorit
# logout
def logout(request):
    request.session.flush()
    return redirect('/')