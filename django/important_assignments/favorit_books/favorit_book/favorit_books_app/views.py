from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
import bcrypt


# Create your views here.
def index(request):
    return render(request, 'main.html')


def register(request):
    errors = User.objects.validator_register(request.POST)

    if len(errors) >0 :
        for ke, value in errors.items():
            messages.error(request, value)
            return redirect('/')
    new_user = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'], 
        email = request.POST['email'],
        password= bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    )

    request.session['user_id'] = new_user.id
    request.session['greeting'] = new_user.first_name

    return redirect('/books')


def login(request):
    errors = User.objects.validator_login(request.POST)

    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/')
    current_user = User.objects.get(email = request.POST['email'])
    request.session['user_id'] = current_user.id
    request.session['greeting'] = current_user.first_name
    return redirect('/books')



def books(request):
    context={
        "all_books" : Book.objects.all(),
        "current_user" : User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'books.html',context)


def create_book(request):

    errors = Book.objects.validator_book(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books')
    user =User.objects.get(id = request.session['user_id'])
    new_book = Book.objects.create(
        title = request.POST['title'],
        description = request.POST['description'],
        creator = user
    )
    user.favorited_books.add(new_book)

    return redirect(f'/books/{new_book.id}')


def show_book(request,book_id):
    context={
        "book" : Book.objects.get(id=book_id),
        "current_user" : User.objects.get(id=request.session['user_id'])

    }
    return render(request, 'show_book.html',context)


def update(request, book_id):
    book = Book.objects.get(id=book_id)
    book.description = request.POST['description']
    book.save()
    return redirect(f'/books/{book_id}')

def delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect(f'/books')

def favorit(request, book_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get( id= request.session['user_id'])
    user.favorited_books.add(book)
    return redirect(f'/books/{book_id}')


def unfavorit(request,book_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get( id= request.session['user_id'])
    user.favorited_books.remove(book)
    return redirect(f'/books/{book_id}')

def logout(request):
    request.session.flush()
    return redirect('/')