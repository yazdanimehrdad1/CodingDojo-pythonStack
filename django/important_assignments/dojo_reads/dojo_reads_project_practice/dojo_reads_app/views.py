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
            birthday = request.POST['birthday'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        )
        request.session["user_id"] = new_user.id
        request.session["greeting"] =  f'{new_user.first_name}  {new_user.last_name}'
        return redirect('/main')


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

        return redirect('/main')

def logout(request):
    request.session.flush()
    return redirect('/')

def face_page(request):
    return render(request, 'login.html')

def main(request):
    context={
        # 'books' : Book.objects.all.order_by('created_at').reverse()[:3],
        'recent_reviews': Review.objects.order_by('created_at').reverse()[:3]
    }
    return render(request, 'main.html', context)

def like_book(request, book_id):
    current_book = Book.objects.get(id=book_id)
    current_book.favorited_by.add(request.session['user_id'])
    return redirect('/main')

def dislike_book(request, book_id):
    current_book = Book.objects.get(id=book_id)
    current_user = User.objects.get(id =request.session['user_id'])
    current_user.user_favorits.remove(current_book)
    return redirect('/main')



def helper(request):
    context={
        "users": User.objects.all(),
        "books": Book.objects.all(),
        "authors": Author.objects.all(),
        "reviews": Review.objects.all()
    }
    return render(request, 'helper.html',context)