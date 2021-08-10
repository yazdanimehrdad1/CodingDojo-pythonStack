from django.shortcuts import HttpResponse,render, redirect
from .models import *
# Create your views here.
def main(request):
    return redirect('/books')
def show_books(request):
    context={
        "books": Book.objects.all()
    }
    return render(request, 'books.html',context)


def show_authors(request):
    context={
        "authors": Author.objects.all()
    }
    return render(request, 'authors.html',context)



def create_book(request):
    if request.method == "GET":
        return redirect('/')
    new_book = Book.objects.create(
        title = request.POST['title'], 
        description = request.POST['description']
    )
    return redirect('/books')

def create_author(request):
    if request.method == "GET":
        return redirect('/')
    new_author = Author.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        notes = request.POST['notes'],
    )
    return redirect('/authors')

def show_book(request, book_id):
    book = Book.objects.get(id=book_id)
    context={
        'book': book,
        # 'authors': Author.objects.all(),
        "authors": Author.objects.exclude(books__id=book_id)
    }
    return render(request, 'book.html', context)


def show_author(request, author_id):
    context= {
        "author": Author.objects.get(id=author_id),
        "books": Book.objects.exclude(authors__id = author_id)
    }
    return render(request, 'author.html', context)


def assign_book(request, book_id):
    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id= request.POST['author_id'])
    book.authors.add(author)
    return redirect(f'/books/{book_id}')

def assign_author(request, author_id):
    author = Author.objects.get(id=author_id)
    book = Book.objects.get(id=request.POST['book_id'])
    author.books.add(book)
    return redirect(f'/authors/{author_id}')
    