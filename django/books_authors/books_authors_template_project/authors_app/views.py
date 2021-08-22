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
    Book.objects.create(title=request.POST['title'],description=request.POST['description'])
    return redirect('/books')


########################################################################################

def show_book(request, book_id):
    currentBook = Book.objects.get(id=book_id)
    context={

        "book": currentBook ,
        # "authors": Author.objects.all(),  # this need to be fixed
        "authors": Author.objects.exclude(books__id = book_id)

    }
    return render(request, 'book.html' , context)


def assign_author(request, book_id):
    book = Book.objects.get(id = book_id)
    author = Author.objects.get(id = request.POST['author_id'])
    book.authors.add(author)
    return redirect('/')

def remove_author(request, author_id, book_id):
    author = Author.objects.get(id=author_id)
    book = Book.objects.get(id= book_id)
    book.authors.remove(author)
    return redirect(f'/books/{book_id}')

    ########################################################################################

def show_author(request, author_id):
    current_author = Author.objects.get(id=author_id)

    context={
        "author":current_author,
        # "books": Book.objects.all()   ###this need to be fixed
        "books": Book.objects.exclude(authors__id= author_id)
    }
    return render(request, 'author.html', context)

def assign_book(request, author_id):
    author = Author.objects.get(id = author_id)
    book = Book.objects.get(id=request.POST['book_id'])
    # author.books.add(book)
    return redirect(f'/authors/{author_id}')





