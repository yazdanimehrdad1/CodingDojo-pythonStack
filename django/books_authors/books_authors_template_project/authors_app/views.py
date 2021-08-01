from django.http import request
from django.shortcuts import render, redirect
from .models import *


def index(request):
    context={
        "books": Book.objects.all()
    }
    return render(request, 'books.html', context)


def authors(request):
    context={
        "authors": Author.objects.all()
    }
    return render(request, 'authors.html' , context)

def create_book(request):
    pass

def show_book(request, book_id):
    currentBook = Book.objects.get(id=book_id)
    context={

        "book": currentBook ,
        "authors": Author.objects.all()  # this need to be fixed

    }
    return render(request, 'book.html' , context)





def show_author(request, author_id):
    current_author = Author.objects.get(id=author_id)

    context={
        "author":current_author,
        "books": Book.objects.all()   ###this need to be fixed
    }
    return render(request, 'author.html', context)



def create_author():
    pass

